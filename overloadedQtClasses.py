from PyQt5 import QtWidgets, QtCore

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


