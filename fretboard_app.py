from PyQt5 import QtWidgets, QtCore
from fretboard_ui import Ui_MainWindow
from fretboard import Fretboard
from musthe import *
import sys
import pandas as pd

def translate(string):
    string=string.replace('b', '♭')
    string=string.replace('#', '♯')
    return string

allScales = [ s for s in Scale.scales.keys() ]
allChords = [ c for c in Chord.valid_types ]

def populateFretboard(ui, notes, intervals, frets):

    # Set up all the labels with notes or intervals on them
    ui.labels = []
    if ui.showInterval:
        fretboard = intervals
    else:
        fretboard = notes

    # We don't want to show the tuning after the nut as a fret, so we cut that column out.
    if min(frets) == 0:
        fret_slice = range(1, frets[1]+1)
        df = pd.DataFrame(fretboard)
        fretboard = df[ fret_slice ].values.tolist()

    i = 0
    for row in fretboard:
        j = 0
        labelRow = []
        for column in row:
            label = QtWidgets.QLabel(ui.centralwidget, text=translate(column))
            ui.gridLayout.addWidget(label, i, j+1, 1, 1)
            labelRow.append(label)
            j = j + 1
        i = i + 1
        ui.labels.append(labelRow)

    for row in ui.labels:
        for label in row:
            if label.text() != '':
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setFrameShape(QtWidgets.QFrame.Box)
                label.setLineWidth(3)

    # Set up the fret buttons
    ui.fretButtons = []

    j = 0
    for fret in range(frets[0], frets[1]+1):
        if fret > 0:
            button = QtWidgets.QPushButton(ui.centralwidget)
            button.setMinimumSize(QtCore.QSize(40, 40))
            button.setMaximumSize(QtCore.QSize(40, 40))
            button.setObjectName("fretButton" + str(fret))
            button.setText(str(fret))
            ui.gridLayout.addWidget(button, 6, j+1, 1, 1)
            ui.fretButtons.append(button)
            j = j + 1

    # Set up the tuning button values
    i = 0
    for peg in ui.tuningButtons:
        peg.setText(ui.tuning[i])
        i = i + 1            


def update():
    showChord_old = ui.showChord
    showInterval_old = ui.showInterval

    ui.showChord = ui.scaleOrChordSlider.value()
    ui.showInterval = ui.notesOrIntervalsSlider.value()

    # If the note/chord slider is changed, update the corresponding combo box.
    if ui.showChord != showChord_old:
        if ui.showChord:
            ui.scaleOrChordTypeSelector.clear()
            ui.scaleOrChordTypeSelector.addItems(allChords)
        else:
            ui.scaleOrChordTypeSelector.clear()
            ui.scaleOrChordTypeSelector.addItems(allScales)
        return

    # If the note/interval slider or number of frets is changed, re-build the labels.
    for row in ui.labels:
        for label in row:
            ui.gridLayout.removeWidget(label)

    f = Fretboard(ui.tuning)
    notes, intervals = f.build(scale=ui.scale, frets=ui.frets)
    populateFretboard(ui, notes, intervals, ui.frets)

def resetFrets():
    ui.frets = (0, 24)
    update()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.tuning_1.setFocus()

    ui.showChord = False
    ui.showInterval = False

    ui.scaleOrChordTypeSelector.addItems(allScales)

    ui.notesOrIntervalsSlider.valueChanged['int'].connect(update) 
    ui.scaleOrChordSlider.valueChanged['int'].connect(update)
    ui.nutButton.clicked.connect(resetFrets)

    ui.tuning = ['E', 'A', 'D', 'G', 'B', 'E']
    ui.frets = (5,9)
    ui.scale = Scale(Note('Cb'), 'major')

    ui.tuningButtons = [
        ui.tuning_1,
        ui.tuning_2,
        ui.tuning_3,
        ui.tuning_4,
        ui.tuning_5,
        ui.tuning_6
    ]
    ui.tuningButtons.reverse()

    f = Fretboard(ui.tuning)
    notes, intervals = f.build(scale=ui.scale, frets=ui.frets)
    #notes, intervals = f.build(chord=Chord(Note('Cb'), 'dim'))

    rootNotes = []
    for e in f.enharmonics:
        rootNotes.append(e[0])

    ui.rootNoteSelector.addItems(rootNotes)

    populateFretboard(ui, notes, intervals, ui.frets)

    MainWindow.show()
    sys.exit(app.exec_())
