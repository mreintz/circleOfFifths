from PyQt5 import QtWidgets, QtCore
from fretboard_ui import Ui_MainWindow
from fretboard import Fretboard
from musthe import *
import sys
import pandas as pd

def populateFretboard(ui, fretboard, frets):

    labels = []

    if min(frets) == 0:
        fret_slice = range(1, frets[1]+1)
        df = pd.DataFrame(fretboard)
        fretboard = df[ fret_slice ].values.tolist()

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
            if label.text() != '':
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setFrameShape(QtWidgets.QFrame.Box)
                label.setLineWidth(3)

    fretButtons = []

    j = 0
    for fret in range(frets[0], frets[1]+1):
        if fret > 0:
            button = QtWidgets.QPushButton(ui.gridLayoutWidget)
            button.setMinimumSize(QtCore.QSize(40, 40))
            button.setMaximumSize(QtCore.QSize(40, 40))
            button.setObjectName("fretButton" + str(fret))
            button.setText(str(fret))
            ui.gridLayout.addWidget(button, 6, j+1, 1, 1)
            fretButtons.append(button)
            j = j + 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.tuning_1.setFocus()

    tuning = ['E', 'A', 'D', 'G', 'B', 'E']

    f = Fretboard(tuning)
    frets = (5, 9)
    notes, intervals = f.build(scale=Scale(Note('A'), 'natural_minor'), frets=frets)

    populateFretboard(ui, notes, frets)

    MainWindow.show()
    sys.exit(app.exec_())
