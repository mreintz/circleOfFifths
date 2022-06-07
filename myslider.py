from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *

class mySlider(QtWidgets.QSlider):
    def __init__(self, parent):
        super().__init__(parent)

    up = pyqtSignal()
    down = pyqtSignal()
    pageup = pyqtSignal()
    pagedown = pyqtSignal()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.up.emit()
        elif event.key() == QtCore.Qt.Key_Down:
            self.down.emit()
        elif event.key() == QtCore.Qt.Key_PageUp:
            self.pageup.emit()
        elif event.key() == QtCore.Qt.Key_PageDown:
            self.pagedown.emit()
        else:
            super(mySlider, self).keyPressEvent(event)
