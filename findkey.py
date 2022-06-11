from PyQt5 import QtWidgets, uic, QtCore, QtGui
from pyparsing import Diagnostics
from keyfromchords import findKeyFromChords
import sys

from keysfromchords_ui import Ui_Dialog

majorcolor = "QPushButton {background-color : rgba(205, 253, 205, 80%)};"
minorcolor = "QPushButton {background-color : rgba(173, 215, 229, 80%)};"


def translate(string):
    string=string.replace('b', '<sub>♭</sub>')
    string=string.replace('#', '♯')
    return string

"""class FindKeyUi(QtWidgets.QDialog):
    def __init__(self):
        super(FindKeyUi, self).__init__()
        uic.loadUi('keyfromchords.ui', self)"""     


class FindKeyUi(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(FindKeyUi, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.chords = []
        self.majorMinor = False
        
        self.cButton.clicked.connect(lambda: self.addChord('C'))
        self.dButton.clicked.connect(lambda: self.addChord('D'))
        self.eButton.clicked.connect(lambda: self.addChord('E'))
        self.fButton.clicked.connect(lambda: self.addChord('F'))
        self.gButton.clicked.connect(lambda: self.addChord('G'))
        self.aButton.clicked.connect(lambda: self.addChord('A'))
        self.bButton.clicked.connect(lambda: self.addChord('B'))
        
        self.csButton.clicked.connect(lambda: self.addChord('C#'))
        self.dsButton.clicked.connect(lambda: self.addChord('D#'))
        self.fsButton.clicked.connect(lambda: self.addChord('F#'))
        self.gsButton.clicked.connect(lambda: self.addChord('G#'))
        self.asButton.clicked.connect(lambda: self.addChord('A#'))

        self.dbButton.clicked.connect(lambda: self.addChord('Db'))
        self.ebButton.clicked.connect(lambda: self.addChord('Eb'))
        self.gbButton.clicked.connect(lambda: self.addChord('F#'))
        self.abButton.clicked.connect(lambda: self.addChord('Ab'))
        self.bbButton.clicked.connect(lambda: self.addChord('Bb'))

        self.cButton_2.clicked.connect(lambda: self.addChord('Cm'))
        self.dButton_2.clicked.connect(lambda: self.addChord('Dm'))
        self.eButton_2.clicked.connect(lambda: self.addChord('Em'))
        self.fButton_2.clicked.connect(lambda: self.addChord('Fm'))
        self.gButton_2.clicked.connect(lambda: self.addChord('Gm'))
        self.aButton_2.clicked.connect(lambda: self.addChord('Am'))
        self.bButton_2.clicked.connect(lambda: self.addChord('Bm'))
        
        self.csButton_2.clicked.connect(lambda: self.addChord('C#m'))
        self.dsButton_2.clicked.connect(lambda: self.addChord('D#m'))
        self.fsButton_2.clicked.connect(lambda: self.addChord('F#m'))
        self.gsButton_2.clicked.connect(lambda: self.addChord('G#m'))
        self.asButton_2.clicked.connect(lambda: self.addChord('A#m'))

        self.dbButton_2.clicked.connect(lambda: self.addChord('Dbm'))
        self.ebButton_2.clicked.connect(lambda: self.addChord('Ebm'))
        self.gbButton_2.clicked.connect(lambda: self.addChord('F#m'))
        self.abButton_2.clicked.connect(lambda: self.addChord('Abm'))
        self.bbButton_2.clicked.connect(lambda: self.addChord('Bbm'))            

        self.majorMinorSlider.valueChanged.connect(self.majorOrMinor)

        self.setWindowTitle("Find key from chords")

        self.keyButtons = []

        self.show()
        
    def majorOrMinor(self):
        if self.majorMinorSlider.value() == 0:
            self.majorMinor = 'major'
        elif self.majorMinorSlider.value() == 2:
            self.majorMinor = 'minor'
        else:
            self.majorMinor = False
        self.getPossibleKeys()

    def addChord(self, chord):
        if chord in self.chords:
            self.chords.remove(chord)
        else:
            self.chords.append(chord)
        self.getPossibleKeys()
        
    def getPossibleKeys(self):
        self.keys = findKeyFromChords(self.chords, self.majorMinor)
        if self.keyButtons != []:
            for button in self.keyButtons:
                self.deleteKeyButton(button)

        if self.keys != []:
            for k in self.keys:
                self.makeKeyButton(k)
           
    def makeKeyButton(self, key):
        self.keyButton = QtWidgets.QPushButton(self.keyWidget)
        self.keyButton.setMinimumSize(QtCore.QSize(60, 50))
        self.keyButton.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.keyButton.setFont(font)
        if 'm' in key:
            self.keyButton.setStyleSheet(minorcolor)
        else:
            self.keyButton.setStyleSheet(majorcolor)
        self.keyButton.setCheckable(True)
        self.keyButton.setObjectName(key+"keyButton")
        self.keyButton.setText(key)
        self.horizontalLayout_4.addWidget(self.keyButton)
        
        self.keyButton.clicked.connect(lambda: self.chooseKey(key))
        self.keyButtons.append(self.keyButton)
        
    def chooseKey(self, key):
        self.keys = key
        self.close()

    def deleteKeyButton(self, button):
        try:
            self.horizontalLayout_4.removeWidget(button)
            button.deleteLater()
            button = None
        except RuntimeError:
            pass    
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = FindKeyUi()
    app.exec_()