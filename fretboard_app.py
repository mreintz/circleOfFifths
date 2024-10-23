from PyQt5 import QtWidgets, QtCore
from fretboard_ui import Ui_MainWindow
from fretboard import Fretboard
from musthe import *
import sys

def populateFretboard(ui, fretboard):

    labels = []
        
    i = 0
    for row in fretboard:
        j = 0
        labelRow = []
        for column in row:
            label = QtWidgets.QLabel(ui.gridLayoutWidget, text=column)
            ui.gridLayout.addWidget(label, i, j+1, 1, 1)
            labelRow.append(label)
            j = j + 1
        i = i + 1
        labels.append(labelRow)

    for row in labels:
        for label in row:
            label.setAlignment(QtCore.Qt.AlignCenter)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.tuning_1.setFocus()

    tuning = ['E', 'A', 'D', 'G', 'B', 'E']

    f = Fretboard(tuning)
    notes, intervals = f.build(scale=Scale(Note('A'), 'natural_minor'))

    populateFretboard(ui, notes)

    MainWindow.show()
    sys.exit(app.exec_())
