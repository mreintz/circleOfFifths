from PyQt5 import QtWidgets, uic
from keyfromchords import findKeyFromChords
import sys

def translate(string):
    string=string.replace('b', '♭')
    string=string.replace('#', '♯')
    return string

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('keyfromchords.ui', self)
        
        self.chords = []
        
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
        
        self.show()
        
    def addChord(self, chord):
        if chord in self.chords:
            self.chords.remove(chord)
        else:
            self.chords.append(chord)
        
        self.chordLabel.setText(translate(', '.join(self.chords)))
        self.keys = findKeyFromChords(self.chords)
        if self.chords != []:
            keystring = []
            for k in self.keys:
                keystring.append(', '.join(k))
            
            self.keyLabel.setText(translate(', '.join(keystring)))
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()