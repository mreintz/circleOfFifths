from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class myLabel(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)

    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()