from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *

class myDropdown(QtWidgets.QComboBox):

    def __init__(self, parent):
        super().__init__(parent)

    keypressed = pyqtSignal()
    right = pyqtSignal()
    left = pyqtSignal()
    space = pyqtSignal()
    progressions = pyqtSignal()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_M:
            self.keypressed.emit()
        elif event.key() == QtCore.Qt.Key_Right:
            self.right.emit()
        elif event.key() == QtCore.Qt.Key_Left:
            self.left.emit()
        elif event.key() == QtCore.Qt.Key_Space:
            self.space.emit()
        elif event.key() == QtCore.Qt.Key_P:
            self.progressions.emit()
        else:
            super(myDropdown, self).keyPressEvent(event)


