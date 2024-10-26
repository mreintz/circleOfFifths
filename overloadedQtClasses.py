from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *

class QComboBoxWithKeyEvents(QtWidgets.QComboBox):

    def __init__(self, parent):
        super().__init__(parent)

    notesOrIntervals = pyqtSignal()
    chordOrScale = pyqtSignal()
    nut = pyqtSignal()
    root = pyqtSignal()
    mode = pyqtSignal()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_I:
            self.notesOrIntervals.emit()
        elif event.key() == QtCore.Qt.Key_C:
            self.chordOrScale.emit()
        elif event.key() == QtCore.Qt.Key_N:
            self.nut.emit()
        elif event.key() == QtCore.Qt.Key_R:
            self.root.emit()
        elif event.key() == QtCore.Qt.Key_M:
            self.mode.emit()
        else:
            super(QComboBoxWithKeyEvents, self).keyPressEvent(event)

class QLineEditTabReact(QtWidgets.QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)

    def event(self,event):
        if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Tab:
            self.tabFollow()
            super(QLineEditTabReact, self).keyPressEvent(event)
            return True
        else:
            return QtWidgets.QLineEdit.event(self,event)
    def tabFollow(self):
        print("tab-key pressed!")
