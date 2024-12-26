from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *

class myLabel(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)

    clicked, right_clicked, control, shift, both = [ pyqtSignal() for i in range(5) ]

    def mousePressEvent(self, event):
        modifiers = QtGui.QGuiApplication.keyboardModifiers()
        if modifiers & Qt.ShiftModifier:
            if modifiers & Qt.ControlModifier:
                self.both.emit()
            else:
                self.shift.emit()
        elif modifiers & Qt.ControlModifier:
            self.control.emit()
        else:
            if event.button() == Qt.RightButton:
                self.right_clicked.emit()
            else:
                self.clicked.emit()            
      