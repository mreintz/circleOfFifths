from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys
from circle import CircleOfFifths
from musthe import *
from circle_ui import Ui_MainWindow

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

translateNote = {
    'B#': 'C',
    'E#': 'F',
    'Fb': 'E',
    'Cb': 'B',
    'Ebb': 'D',
    'Bbb': 'A'
}

chord_colors = {
    'm':    labelColors[2],
    'M':    labelColors[0],
    'd':    labelColors[6],
    'P':    labelColors[0],
    'A':    labelColors[5],
    'P1':    "background-color: red; color: white;"
}

modes = {
    'Lydian': -1,
    'Major': 0, 'Ionian': 0,
    'Mixolydian': 1,
    'Dorian': 2,
    'Minor': 3, 'Aeolian': 3,
    'Phrygian': 4,
    'Locrian': 5
}

chord_types = {
    'maj':  [0, 4, 1],
    'min':  [0, 9, 1],
    'dom7': [0, 4, 1, 10],
    'min7': [0, 9, 1, 10],
    'maj7': [0, 4, 1, 5]
}

def translate(string):
    string=string.replace('b', '♭')
    string=string.replace('#', '♯')
    return string


"""class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('CircleOfFifths.ui', self)"""


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.setWindowTitle("Circle of Fifths")
        self.setWindowIcon(QtGui.QIcon(":/images/note.ico"))
        self.setFixedSize(674, 715)        

        self.first = True
        self.chordsInKey = True

        self.labels = [
            self.CLabel,
            self.GLabel,
            self.DLabel,
            self.ALabel,
            self.ELabel,
            self.BLabel,
            self.FsLabel,
            self.DbLabel,
            self.AbLabel,
            self.EbLabel,
            self.BbLabel,
            self.FLabel
        ]

        self.chordLabels = [
            self.chordLabel0,
            self.chordLabel1,
            self.chordLabel2,
            self.chordLabel3,
            self.chordLabel4,
            self.chordLabel5,
            self.chordLabel6,
            self.chordLabel7,
            self.chordLabel8,
            self.chordLabel9,
            self.chordLabel10,
            self.chordLabel11
        ]

        self.chordPrintLabels = [ 
            self.onechord,
            self.twochord,
            self.threechord,
            self.fourchord,
            self.fivechord,
            self.sixchord,
            self.sevenchord
        ]

        self.intervalLabels = [ 
            self.onechord_2,
            self.twochord_2,
            self.threechord_2,
            self.fourchord_2,
            self.fivechord_2,
            self.sixchord_2,
            self.sevenchord_2
        ]

        self.mode = 'Major'
        self.key = 'C'
        self.modeBox.addItems(modes.keys())
        self.modeBox.activated.connect(self.changeMode)
        self.modeBox.keypressed.connect(self.keyPress)
        self.modeBox.right.connect(lambda attr='Right': self.rotate(attr))
        self.modeBox.left.connect(lambda attr='Left': self.rotate(attr))
        self.modeBox.space.connect(self.toggleMode)

        self.modeSlider.valueChanged.connect(self.changeCircleMode)

        self.c0 = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Db', 'Ab', 'Eb', 'Bb', 'F']

        for l in self.labels:
            l.clicked.connect(lambda val=self.c0[self.labels.index(l)]: self.setkey(val))

        self.statusbar.showMessage('Click on root note.')

        self.modeBox.setCurrentIndex(1)
        #self.setkey(self.key)

        #self.show()

    # Selects which scale to use for each type of chord.
    def mapChordToScale(self):
        if self.mode in ['maj', 'maj7']:
            return 'major'
        else:
            return 'natural_minor'

    # Rotates in clockwise or anti-clockwise direction.
    def rotate(self, direction):
        self.clockface = self.c0.index(self.key)
        if direction == 'Right':
            if self.clockface == 11:
                self.key = 'C'
                self.clockface = 0
            else:
                self.clockface = self.clockface + 1
                self.key = self.c0[self.clockface]
        else:
            if self.clockface == 0:
                self.key = 'F'
                self.clockface = 11
            else:
                self.clockface = self.clockface - 1
                self.key = self.c0[self.clockface]

        self.setkey(self.key)

    # This runs when slider is activated. Toggles between chords in key or notes on chord.
    def toggleMode(self):
        if self.modeSlider.value() == 1:
            self.modeSlider.setValue(0)
        else:
            self.modeSlider.setValue(1)

    # Changes ths mode of the circle: chords in key or notes on chord.
    def changeCircleMode(self):
        if self.modeSlider.value() == 1:
            self.chordsInKey = False
            self.modeBox.clear()
            self.modeBox.addItems(chord_types.keys())
            if self.mode == 'Major':
                self.modeBox.setCurrentIndex(0)
            else:
                self.modeBox.setCurrentIndex(1)
        else:
            self.chordsInKey = True
            self.modeBox.clear()
            self.modeBox.addItems(modes.keys())
            if self.mode == 'maj':
                self.modeBox.setCurrentIndex(1)
            else:
                self.modeBox.setCurrentIndex(5)

        self.changeMode()
        self.modeBox.setFocus()

    # This runs when pressing the space bar. Toggles between chords in key or notes on chord.
    def keyPress(self):
        if ( self.mode == 'Major' or self.mode == 'maj' ):
            if self.chordsInKey:
                self.mode = 'Minor'
                self.modeBox.setCurrentIndex(5)
            else:
                self.mode = 'min'
                self.modeBox.setCurrentIndex(1)
        else:
            if self.chordsInKey:
                self.mode = 'Major'
                self.modeBox.setCurrentIndex(1)
            else:
                self.mode = 'maj'
                self.modeBox.setCurrentIndex(0)

        self.changeMode()

    #Get the mode or chord type from the dropdown menu, then set the key and paint the circle.
    def changeMode(self):
        self.mode = self.modeBox.currentText()
        self.setkey(self.key)

    # Sets the key according to user input.
    def setkey(self, key):
        if self.first:
            self.first = False
            self.statusbar.showMessage('"m" switches between Major and Minor modes. Try space and arrow keys.', 10000)

        # Set the key label in the upper left corner to the selected key.
        self.keyLabel.setText(translate(key))
        self.key = key

        # Get the "clockface" index, i.e. the position on the "basic" circle of the new key. 0 for C, 1 for G, etc.
        self.clockface = self.c0.index(self.key)

        # Repaint the circle.
        self.updateCircle()
        # Update the color labels on the notes, the chord types (I, ii, iii, etc.) in the inner circle plus the actual chords at the bottom.
        self.updateChords()

    # Update the actual circle of fifths according to user input.
    def updateCircle(self):
        # Generate the abstract circle of fifths from the key and the mode.
        self.circle = CircleOfFifths(Note(self.key), mode=self.mode)

        # Create the "clockstring", i.e. the string of note labels to be written starting from 12 o'clock on the circle. 
        # It will always start with a C, but the flats and sharps will vary.
        self.clockstring = self.circle.circlestring[12-self.clockface:]+self.circle.circlestring[:12-self.clockface]
        
        # Write the clockstring onto the labels. 
        i = 0
        for l in self.labels:
            l.setText(translate(self.clockstring[i]))
            i = i + 1

        if self.chordsInKey:
            # Set the number of sharps or flats in the middle of the circle. Do this only when in chords in key mode.
            self.SharpFlatLabel.setText(translate(self.circle.key_signature()[1]))
        else:
            self.SharpFlatLabel.setText('')

            self.chord = Chord(Note(self.key), self.modeBox.currentText())
            
            # Otherwise, get the notes in the selected chord.
            self.notesInChord = []
            i = 0
            for n in self.chord.notes:
                notestring = str(n.letter)+str(n.accidental)
                self.notesInChord.append([self.chord.recipes[self.modeBox.currentText()][i], notestring])
                i = i + 1

    # Update the "inner labels" on the circle.
    def updateChords(self):        

        # Reset everything.
        for l in self.chordLabels:
            l.setText('')

        for l in self.labels:
            l.setStyleSheet(transparent)

        # If in chords in key mode, set the I, ii, iii, etc. labels.
        if self.chordsInKey:
            chord_index = 0
            for c in self.circle.chords():
                # The type of chord, e.g. 'I'-chord
                text = c[0]
                # The note, e.g. 'G'
                note = c[1]
                # The type of chord, i.e. Major, minor, diminished.
                ctype = c[2]
                # The actual chord, e.g. Gbm.
                chord = c[3]

                # Set the labels at the bottom.
                self.intervalLabels[chord_index].setText(text)

                for i in range(12):
                    l = self.labels[i]

                    # When we get a match for our chord, set the appropriate background color for the note, then set the inner circle chord indicators.
                    if l.text() == translate(note):
                        self.chordLabels[i].setText(text)
                        l.setStyleSheet(chord_colors[ctype])
                        i = i + 1

                # Update the chords at the very bottom.
                self.chordPrintLabels[chord_index].setText(translate(chord))
                self.chordPrintLabels[chord_index].setStyleSheet(chord_colors[ctype])

                chord_index = chord_index + 1
        else:
            # Else write out the scale and indicate the intervals.
            scale = Scale(Note(self.key), name = self.mapChordToScale()) # Gets the approprite scale, major or natural minor.

            # Gets the intervals and writes them to the bottom labels.
            intervals = [str(i) for i in scale.intervals]
            for i in range(7):
                self.intervalLabels[i].setText(intervals[i])

            # Makes the list of scale notes
            scale_labels = []
            for n in scale.notes:
                note = str(n.letter)+n.accidental
                scale_labels.append(note)

            # Writes the intervals to the labels.
            for i in range(7):
                self.chordPrintLabels[i].setText(translate(translateNote.get(scale_labels[i], scale_labels[i])))
                self.chordPrintLabels[i].setStyleSheet(transparent)

            i = 0
            for n in self.notesInChord:
                # The interval, e.g. "P4"
                interval = n[0]
                interval_on_scale = interval[1]
                self.chordPrintLabels[int(interval_on_scale)-1].setStyleSheet(chord_colors[interval[0]])

                # The note, e.g. F#.
                note = n[1]

                recipe = chord_types[self.mode][i]

                hour = self.clockface+recipe
                if hour > 11:
                    hour = hour - 12

                l = self.labels[hour]
                self.chordLabels[hour].setText(interval)
                if recipe == 0:
                    l.setStyleSheet(chord_colors['P1'])
                else:    
                    l.setStyleSheet(chord_colors[interval[0]])

                i = i + 1

app = QtWidgets.QApplication(sys.argv)
#window = Ui()
window = MainWindow()
window.show()
app.exec_()        