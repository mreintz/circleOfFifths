from PyQt5 import QtWidgets, QtCore, QtGui
from fretboard_ui import Ui_MainWindow
from fretboard import Fretboard
from musthe import *
import sys
import pandas as pd

transparent = "background-color: rgba(255, 255, 255, 0%);"

labelColors = [
    "background-color: rgba(205, 253, 205, 80%);",
    "background-color: rgba(147, 223, 199, 80%);",
    "background-color: rgba(173, 215, 229, 80%);",
    "background-color: rgba(247, 247, 185, 80%);",
    "background-color: rgba(255, 210, 127, 80%);",
    "background-color: rgba(254, 160, 122, 80%);",
    "background-color: rgba(217, 170, 174, 80%);"
]

interval_colors = {
    'm':        labelColors[2],
    'M':        labelColors[0],
    'd':        labelColors[6],
    'P':        "background-color: rgba(220, 220, 170, 80%);",  #labelColors[0],
    'A':        labelColors[5],
    'P1':       "background-color: red; color: white;"
}

def translate(string):
    string=string.replace('b', '♭')
    string=string.replace('#', '♯')
    return string

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
            label.setObjectName(column)
            font = QtGui.QFont()
            font.setPointSize(12)
            label.setFont(font)
            ui.gridLayout.addWidget(label, i, j+1, 1, 1)
            labelRow.append(label)
            j = j + 1
        i = i + 1
        ui.labels.append(labelRow)

    flattenedNotes = []
    flattenedIntervals = []
    for row in notes:
        flattenedNotes += row
    for row in intervals:
        flattenedIntervals += row

    for row in ui.labels:
        for label in row:
            if label.text() != '':
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setFrameShape(QtWidgets.QFrame.Box)
                label.setLineWidth(3)
                if ui.showInterval:
                    interval =  label.objectName()
                    if interval != "P1":
                        intervalType = interval[0]
                    else:
                        intervalType = interval
                else:
                    try:
                        interval = flattenedIntervals[flattenedNotes.index(label.objectName())]
                        if interval != "P1":
                            intervalType = interval[0]
                        else:
                            intervalType = interval
                    except ValueError:
                        intervalType = ''

                label.setStyleSheet("QLabel"
                            "{"
                            f"{interval_colors[intervalType]}"
                            "}")

    # Set up the fret buttons
    ui.fretButtons = []
    j = 0
    for fret in range(frets[0], frets[1]+1):
        if fret > 0:
            button = QtWidgets.QPushButton(ui.centralwidget)
            button.setMinimumSize(QtCore.QSize(40, 40))
            button.setMaximumSize(QtCore.QSize(40, 40))
            font = QtGui.QFont()
            font.setPointSize(12)
            button.setFont(font)
            button.setObjectName("fretButton" + str(fret))
            button.setText(str(fret))
            button.setFocusPolicy(QtCore.Qt.ClickFocus)
            ui.gridLayout.addWidget(button, 6, j+1, 1, 1)
            ui.fretButtons.append(button)
            button.clicked.connect(lambda state, x=fret: setFret(x))
            j = j + 1

    # Set up the tuning button values and bold text if note is on the scale/chord
    i = 0
    for peg in ui.tuningButtons:
        text = ui.tuning[i]
        peg.setStyleSheet("QLineEdit")

        try:
            interval = flattenedIntervals[flattenedNotes.index(text)]
            if interval != "P1":
                intervalType = interval[0]
            else:
                intervalType = interval
        except ValueError:
            interval = ''

        for row in notes:
            for note in row:
                if text == note:
                    peg.setStyleSheet("QLineEdit"
                                "{"
                                "border : 3px solid ;"
                                f"{interval_colors[intervalType]}"
                                "border-color : black"
                                "}")
        peg.setText(text)
        i = i + 1

def setFret(fret):
    # Set new fret selection
    if not ui.fretSelected:
        # Is this the first or the second fret selected in the range?
        ui.fretSelected = True
        ui.firstFretSelected = fret
        for row in ui.labels:
            try:
                index = fret - ui.frets[0]
                if ui.frets[0] == 0:
                    index = index - 1
                row[index].setStyleSheet("QLabel"
                    "{"
                    f"{interval_colors['m']}"
                    "}")
            except IndexError:
                pass
    else:
        # If second, we set up the new fret tuple and rebuild.
        ui.fretSelected = False
        ui.secondFretSelected = fret
        if ui.firstFretSelected != ui.secondFretSelected:
            ui.frets = (ui.firstFretSelected, ui.secondFretSelected)
            ui.frets = tuple(sorted(ui.frets)) # You can select in any order.
            update()

def update():
    # Updates the GUI.

    showChord_old = ui.showChord
    ui.showChord = ui.scaleOrChordSlider.value()
    ui.showInterval = ui.notesOrIntervalsSlider.value()

    # If the note/chord slider is changed, update the corresponding combo box to reflect the change.
    if ui.showChord != showChord_old:
        if ui.showChord:
            ui.scaleOrChordTypeSelector.clear()
            ui.scaleOrChordTypeSelector.addItems(ui.allChords)
            type = ui.scaleOrChordTypeSelector.currentText()
            root = ui.rootNoteSelector.currentText()
            ui.chord = Chord(Note(root), type)
        else:
            ui.scaleOrChordTypeSelector.clear()
            ui.scaleOrChordTypeSelector.addItems(ui.allScales)
            type = ui.scaleOrChordTypeSelector.currentText()
            root = ui.rootNoteSelector.currentText()
            ui.scale = Scale(Note(root), type)

    # Re-build the labels. First remove the old ones.
    for row in ui.labels:
        for label in row:
            ui.gridLayout.removeWidget(label)

    # Remove the buttons as well.
    for button in ui.fretButtons:
        ui.gridLayout.removeWidget(button)

    # Generate the new fretboard
    f = Fretboard(ui.tuning)
    if ui.showChord:
        notes, intervals = f.build(chord=ui.chord, frets=ui.frets)
    else:
        notes, intervals = f.build(scale=ui.scale, frets=ui.frets)

    populateFretboard(ui, notes, intervals, ui.frets)

    if ui.showChord:
        type = "chord"
    else:
        type = "scale"
    ui.titleLabel.setText(f"{ui.rootNoteSelector.currentText()} {ui.scaleOrChordTypeSelector.currentText()} {type}")

def tuning(string):
    # Deal with changes in tuning from one of the tuning peg input boxes.
    old = ui.tuning[string]
    new = ui.tuningButtons[string].text().capitalize()

    match = False
    for row in ui.enharmonics:
        for note in row:
            if new == note:
                match = True

    if not match:
        ui.statusbar.showMessage(f"reverting to {old}", 10000)
        ui.tuningButtons[string].setText(old)
    elif old != new:
        ui.statusbar.showMessage(f"Changing to {new}", 10000)
        ui.tuning[string] = new
        update()

def resetFrets():
    ui.frets = (0, 24)
    update()

def changeScaleOrChord():
    # Change from scale to chord or back.
    try:
        delattr(ui, chord)
    except NameError:
        try:
            delattr(ui, scale)
        except NameError:
            pass

    type = ui.scaleOrChordTypeSelector.currentText()
    root = ui.rootNoteSelector.currentText()
    if ui.showChord:
        ui.chord = Chord(Note(root), type)
        ui.statusbar.showMessage(f"{root} {type}", 10000)
    else:
        ui.scale = Scale(Note(root), type)
        ui.statusbar.showMessage(f"{root} {type}", 10000)
    update()

def toggle(thing):
    if thing == 'intervals':
        if ui.notesOrIntervalsSlider.value() == 1:
            ui.notesOrIntervalsSlider.setValue(0)
        else:
            ui.notesOrIntervalsSlider.setValue(1)
    elif thing == 'chord':
        if ui.scaleOrChordSlider.value() == 1:
            ui.scaleOrChordSlider.setValue(0)
        else:
            ui.scaleOrChordSlider.setValue(1)
    ui.rootNoteSelector.setFocus()
    return

def select(thing):
    if thing == 'mode':
        ui.scaleOrChordTypeSelector.setFocus()
    elif thing == 'root':
        ui.rootNoteSelector.setFocus()
    elif thing == 'tuning':
        ui.tuning_6.setFocus()
        ui.tuning_6.selectAll()
    return

def initialSetup(ui):
    ui.showChord = False
    ui.showInterval = False
    ui.fretSelected = False

    # List of all the options for Chord() and Scale()
    ui.allScales = [ s for s in Scale.scales.keys() ]
    ui.allChords = [ c for c in Chord.valid_types ]
    ui.scaleOrChordTypeSelector.addItems(ui.allScales)

    ui.notesOrIntervalsSlider.valueChanged['int'].connect(update)
    ui.scaleOrChordSlider.valueChanged['int'].connect(update)
    ui.nutButton.clicked.connect(resetFrets)
    ui.rootNoteSelector.activated.connect(changeScaleOrChord)
    ui.scaleOrChordTypeSelector.activated.connect(changeScaleOrChord)

    ui.rootNoteSelector.notesOrIntervals.connect(lambda thing='intervals': toggle(thing) )
    ui.rootNoteSelector.chordOrScale.connect(lambda thing='chord': toggle(thing) )
    ui.rootNoteSelector.nut.connect(resetFrets)
    ui.rootNoteSelector.mode.connect(lambda thing='mode': select(thing))
    ui.rootNoteSelector.tuning.connect(lambda thing='tuning': select(thing))

    ui.scaleOrChordTypeSelector.notesOrIntervals.connect(lambda thing='intervals': toggle(thing) )
    ui.scaleOrChordTypeSelector.chordOrScale.connect(lambda thing='chord': toggle(thing) )
    ui.scaleOrChordTypeSelector.nut.connect(resetFrets)
    ui.scaleOrChordTypeSelector.root.connect(lambda thing='root': select(thing))
    ui.scaleOrChordTypeSelector.tuning.connect(lambda thing='tuning': select(thing))

    ui.nutButton.setFocusPolicy(QtCore.Qt.ClickFocus)

    ui.tuning = ['E', 'A', 'D', 'G', 'B', 'E']
    ui.frets = (0,24)
    ui.scale = Scale(Note('C'), 'major')

    ui.tuningButtons = [
        ui.tuning_6,
        ui.tuning_5,
        ui.tuning_4,
        ui.tuning_3,
        ui.tuning_2,
        ui.tuning_1
    ]

    i = 0
    for t in ui.tuningButtons:
        t.returnPressed.connect(lambda string=i: tuning(string))
        i = i + 1

    f = Fretboard(ui.tuning)
    notes, intervals = f.build(scale=ui.scale, frets=ui.frets)
    #notes, intervals = f.build(chord=Chord(Note('Cb'), 'dim'))

    ui.enharmonics = f.enharmonics
    rootNotes = []
    for e in ui.enharmonics:
        rootNotes.append(e[0])

    ui.rootNoteSelector.addItems(rootNotes)

    populateFretboard(ui, notes, intervals, ui.frets)
    ui.rootNoteSelector.setFocus()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    initialSetup(ui)

    MainWindow.show()
    sys.exit(app.exec_())
