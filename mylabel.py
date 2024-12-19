from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *

class myLabel(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)

    clicked = pyqtSignal()
    play = pyqtSignal()

    def mousePressEvent(self, event):
        modifiers = QtGui.QGuiApplication.keyboardModifiers()
        if modifiers & Qt.ShiftModifier:
            pass
        elif modifiers & Qt.ControlModifier:
            self.play.emit()
        else:
            self.clicked.emit()