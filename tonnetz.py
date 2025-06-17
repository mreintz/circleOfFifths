import sys
from PyQt5.QtWidgets import (
    QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem,
    QGraphicsTextItem, QMainWindow, QGraphicsDropShadowEffect
)
from PyQt5.QtGui import QBrush, QPen, QFont, QPainter, QColor
from PyQt5.QtCore import Qt, QRectF, QPointF

NODE_RADIUS = 18
GRID_SIZE = 120

CHROMATIC = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
ENHARMONIC = {
    "Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#", "Bb": "A#",
    "Cb": "B", "Fb": "E", "E#": "F", "B#": "C"
}

def normalize_note(note):
    return ENHARMONIC.get(note, note)

def fifth(note):
    idx = CHROMATIC.index(normalize_note(note))
    return CHROMATIC[(idx + 7) % 12]

def minor_third(note):
    idx = CHROMATIC.index(normalize_note(note))
    return CHROMATIC[(idx + 3) % 12]

def major_third(note):
    idx = CHROMATIC.index(normalize_note(note))
    return CHROMATIC[(idx + 4) % 12]

def pretty_note(note):
    return note.replace("#", "♯").replace("b", "♭")

class NoteNode(QGraphicsEllipseItem):
    def __init__(self, x, y, i, j, note, pretty, parent=None):
        super().__init__(x - NODE_RADIUS, y - NODE_RADIUS, NODE_RADIUS * 2, NODE_RADIUS * 2, parent)
        self.note = note
        self.pretty = pretty
        self.i = i
        self.j = j
        self.text_item = None
        self.setBrush(QBrush(Qt.white))
        self.setPen(QPen(Qt.gray, 1))
        self.setFlag(QGraphicsEllipseItem.ItemIsSelectable)
        self.setAcceptHoverEvents(True)
        self.setZValue(1)

    def set_text_item(self, text_item):
        self.text_item = text_item

    def set_glow(self, glow):
        if glow:
            effect = QGraphicsDropShadowEffect()
            effect.setBlurRadius(30)
            effect.setColor(QColor(255, 255, 0))
            effect.setOffset(0)
            self.setGraphicsEffect(effect)
        else:
            self.setGraphicsEffect(None)

class IsoGridScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSceneRect(-5000, -5000, 10000, 10000)
        self.grid_size = 40
        self.nodes = {}  # (i, j): NoteNode
        self.note_to_nodes = {}  # normalized note: set of NoteNode
        self.selected_triangles = set()
        self.draw_grid()

    def draw_grid(self):
        node_positions = {}
        for i in range(-self.grid_size, self.grid_size + 1):
            for j in range(-self.grid_size, self.grid_size + 1):
                x = (i - j) * GRID_SIZE / 2
                y = (i + j) * GRID_SIZE / 4
                node_positions[(i, j)] = (x, y)

        # Draw lines first (so they appear under the nodes)
        for (i, j), (x, y) in node_positions.items():
            for di, dj in [
                (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)
            ]:
                neighbor = (i + di, j + dj)
                if neighbor in node_positions:
                    nx, ny = node_positions[neighbor]
                    self.addLine(x, y, nx, ny, QPen(Qt.lightGray, 1))

        # BFS to fill the grid with note labels
        labels = {}
        center = (0, 0)
        labels[center] = "C"
        from collections import deque
        queue = deque()
        queue.append(center)
        while queue:
            i, j = queue.popleft()
            note = labels[(i, j)]
            # Above/up: (i-1, j-1) = one fifth above
            up = (i - 1, j - 1)
            if up in node_positions and up not in labels:
                labels[up] = fifth(note)
                queue.append(up)
            # Up and to the left: (i - 1, j) = one minor third above
            ul = (i - 1, j)
            if ul in node_positions and ul not in labels:
                labels[ul] = minor_third(note)
                queue.append(ul)
            # Up and to the right: (i, j - 1) = one major third above
            ur = (i, j - 1)
            if ur in node_positions and ur not in labels:
                labels[ur] = major_third(note)
                queue.append(ur)

        # Draw all nodes first
        for (i, j), (x, y) in node_positions.items():
            note = labels.get((i, j))
            if note is None:
                continue
            pretty = pretty_note(note)
            node = NoteNode(x, y, i, j, note, pretty)
            self.addItem(node)
            self.nodes[(i, j)] = node
            n_note = normalize_note(note)
            if n_note not in self.note_to_nodes:
                self.note_to_nodes[n_note] = []
            self.note_to_nodes[n_note].append(node)

        # Draw all labels after nodes so they are on top
        for (i, j), node in self.nodes.items():
            x = node.rect().center().x() + node.pos().x()
            y = node.rect().center().y() + node.pos().y()
            text = QGraphicsTextItem(node.pretty)
            text.setFont(QFont("Arial", 16, QFont.Bold))
            text.setDefaultTextColor(Qt.black)
            text_rect = text.boundingRect()
            text.setPos(x - text_rect.width() / 2, y - text_rect.height() / 2)
            text.setZValue(10)
            self.addItem(text)
            node.set_text_item(text)

    def clear_glow(self):
        for node in self.nodes.values():
            node.set_glow(False)

    def highlight_like_nodes(self, note):
        self.clear_glow()
        self.selected_triangles.clear()
        n_note = normalize_note(note)
        for node in self.note_to_nodes.get(n_note, []):
            node.set_glow(True)

    def highlight_triangle_apexes(self, apexes, expand=True):
        tri_set = frozenset(apexes)
        if tri_set in self.selected_triangles:
            # Deselect if already selected
            self.selected_triangles.remove(tri_set)
        elif expand and self.selected_triangles:
            # Expand if at least one apex is shared with any selected triangle
            for sel_tri in self.selected_triangles:
                if len(sel_tri & tri_set) >= 1:
                    self.selected_triangles.add(tri_set)
                    break
            else:
                # Not adjacent, start new selection
                self.selected_triangles = {tri_set}
        else:
            self.selected_triangles = {tri_set}
        self.clear_glow()
        for tri in self.selected_triangles:
            for apex in tri:
                if apex in self.nodes:
                    self.nodes[apex].set_glow(True)
        # Collect all apexes from all selected triangles
        all_apexes = set()
        for tri in self.selected_triangles:
            all_apexes.update(tri)
        # Sort from lower to upper (descending i+j)
        sorted_apexes = sorted(all_apexes, key=lambda x: x[0] + x[1], reverse=True)
        # Eliminate duplicate notes (by pretty label, preserving order)
        seen = set()
        notes = []
        for apex in sorted_apexes:
            pretty = self.nodes[apex].pretty
            if pretty not in seen:
                notes.append(pretty)
                seen.add(pretty)
        print("-".join(notes))

    def find_triangle_under_point(self, point):
        # For each triangle in the grid, check if point is inside and has a "vertical" (up-down axis) side
        for (i, j), node in self.nodes.items():
            tri_list = [
                [(i, j), (i-1, j), (i, j-1)],      # up-right
                [(i, j), (i+1, j), (i, j+1)],      # down-left
                [(i, j), (i-1, j-1), (i, j-1)],    # up
                [(i, j), (i+1, j+1), (i, j+1)],    # down
                [(i, j), (i-1, j-1), (i-1, j)],    # up-left
                [(i, j), (i+1, j+1), (i+1, j)]     # down-right
            ]
            for tri in tri_list:
                if all(apex in self.nodes for apex in tri):
                    # Check for a "vertical" (up-down axis) pair: (i2-i1)==(j2-j1)==±1
                    has_vertical = False
                    for idx1 in range(3):
                        for idx2 in range(idx1+1, 3):
                            i1, j1 = tri[idx1]
                            i2, j2 = tri[idx2]
                            if abs(i2 - i1) == 1 and abs(j2 - j1) == 1 and (i2 - i1) == (j2 - j1):
                                has_vertical = True
                    if has_vertical:
                        pts = [self.nodes[apex].rect().center() + self.nodes[apex].pos() for apex in tri]
                        if point_in_triangle(point, pts[0], pts[1], pts[2]):
                            return tri
        return None

def point_in_triangle(p, a, b, c):
    # Barycentric technique
    def det(p1, p2, p3):
        return (p2.x() - p1.x()) * (p3.y() - p1.y()) - (p3.x() - p1.x()) * (p2.y() - p1.y())
    d1 = det(p, a, b)
    d2 = det(p, b, c)
    d3 = det(p, c, a)
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not (has_neg and has_pos)

class IsoGridView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setWindowTitle("Isometric Grid")
        self._mouse_press_pos = None

    def wheelEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            factor = 1.25 if event.angleDelta().y() > 0 else 0.8
            self.scale(factor, factor)
        else:
            super().wheelEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._mouse_press_pos = event.pos()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self._mouse_press_pos is not None:
            dist = (event.pos() - self._mouse_press_pos).manhattanLength()
            if dist < 5:
                scene_pos = self.mapToScene(event.pos())
                # Check if the click is close to any node center
                closest_node = None
                min_dist = float('inf')
                for node in self.scene().nodes.values():
                    node_center = node.sceneBoundingRect().center()
                    d = (scene_pos - node_center).manhattanLength()
                    if d < min_dist:
                        min_dist = d
                        closest_node = node
                if min_dist < NODE_RADIUS * 0.9:
                    self.scene().highlight_like_nodes(closest_node.note)
                    super().mouseReleaseEvent(event)
                    return
                # Otherwise, check for triangle
                tri = self.scene().find_triangle_under_point(scene_pos)
                if tri:
                    self.scene().highlight_triangle_apexes(tri, expand=True)
                else:
                    self.scene().clear_glow()
        super().mouseReleaseEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        scene = IsoGridScene()
        view = IsoGridView(scene)
        self.setCentralWidget(view)
        self.resize(1000, 800)
        self.setWindowTitle("Isometric Grid with Circular Nodes")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())