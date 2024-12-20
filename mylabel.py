from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *

class myLabel(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)

    clicked, play, note, arpeggio = [ pyqtSignal() for i in range(4) ]

    def mousePressEvent(self, event):
        modifiers = QtGui.QGuiApplication.keyboardModifiers()
        if modifiers & Qt.ShiftModifier:
            if modifiers & Qt.ControlModifier:
                self.arpeggio.emit()
            else:
                self.note.emit()
        elif modifiers & Qt.ControlModifier:
            self.play.emit()
        else:
            self.clicked.emit()