from musthe import *

translateNote = {
    'B#': 'C',
    'E#': 'F',
    'Fb': 'E',
    'Cb': 'B',
    'Ebb': 'D',
    'Bbb': 'A'
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

class CircleOfFifths():  
    def __init__(self, key, **args):
        self.mode = 'Major'
        if args:
            for k,v in args.items():
                if k == 'mode':
                    self.mode = v
        
        fifth = Interval('P5')
        fourth = Interval('P4')
       
        n = key
        if n == Note('Gb'):
            n = Note('F#')
        self.circle = []
        self.sharpcircle = []
        
        for i in range(12):
            self.sharpcircle.append(n)
            n = (n + fifth).to_octave(4)
            i = i + 1
            
        self.circle = self.sharpcircle[:7]
            
        self.flatcircle = []
        n = key
        for i in range(11):
            n = (n + fourth).to_octave(4)
            self.flatcircle.append(n)
            i = i + 1

        reverse_circle = self.flatcircle[:5]
        reverse_circle.reverse()
        self.circle = self.circle + reverse_circle
        
        self.circlestring = []
        for n in self.circle:
            notestring = str(n.letter)+str(n.accidental)
            self.circlestring.append(translateNote.get(notestring,notestring))
        
    def key_signature(self):
       
        c0_string = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Db', 'Ab', 'Eb', 'Bb', 'F']
        c0_sharpstring = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'F']               
        
        mode = modes[self.mode]
       
        try:
            sig = c0_string.index(self.circlestring[0]) - mode
        except AttributeError:
            sig = c0_sharpstring.index(self.circlestring[0]) - mode
       
        if( sig == 0 ):
            sigstring = '♯'        
        elif( sig < 0 ):
            sigstring = str(-sig) + "b"            
        elif( sig <= 6 ):
            sigstring = str(sig) + "#"
        else:
            sigstring = str(12-sig) + "b"
            
        return (sig, sigstring)
    
    def chords(self):

        mode = modes[self.mode]
        
        chord_template = {
            -1: ['I', 'V', 'II', 'vi', 'iii', 'vii', 'iv°', '', '', '', '', ''],
            0:  ['I', 'V', 'ii', 'vi', 'iii', 'vii°', '', '', '', '', '', 'IV'],
            1:  ['I', 'v', 'ii', 'vi', 'iii°', '', '', '', '', '', 'VII', 'IV'],
            2:  ['i', 'v', 'ii', 'vi°', '', '', '', '', '', 'III', 'VII', 'IV'],
            3:  ['i', 'v', 'ii°', '', '', '', '', '', 'VI', 'III', 'VII', 'iv'],
            4:  ['i', 'v°', '', '', '', '', '', 'II', 'VI', 'III', 'vii', 'iv'],
            5:  ['i°', '', '', '', '', '', 'V', 'II', 'VI', 'iii', 'vii', 'iv']
        }
        
        chord_type = {
            -1: ['M', 'M', 'M', 'm', 'm', 'm', 'd', '', '', '', '', ''],
            0:  ['M', 'M', 'm', 'm', 'm', 'd', '', '', '', '', '', 'M'],
            1:  ['M', 'm', 'm', 'm', 'd', '', '', '', '', '', 'M', 'M'],
            2:  ['m', 'm', 'm', 'd', '', '', '', '', '', 'M', 'M', 'M'],
            3:  ['m', 'm', 'd', '', '', '', '', '', 'M', 'M', 'M', 'm'],
            4:  ['m', 'd', '', '', '', '', '', 'M', 'M', 'M', 'm', 'm'],
            5:  ['d', '', '', '', '', '', 'M', 'M', 'M', 'm', 'm', 'm'],
        }
        
        chord_numbering = {
            -1: [1, 5, 2, 6, 3, 7, 4, 0, 0, 0, 0, 0],
            0:  [1, 5, 2, 6, 3, 7, 0, 0, 0, 0, 0, 4],
            1:  [1, 5, 2, 6, 3, 0, 0, 0, 0, 0, 7, 4],
            2:  [1, 5, 2, 6, 0, 0, 0, 0, 0, 3, 7, 4],
            3:  [1, 5, 2, 0, 0, 0, 0, 0, 6, 3, 7, 4],
            4:  [1, 5, 0, 0, 0, 0, 0, 2, 6, 3, 7, 4],
            5:  [1, 0, 0, 0, 0, 0, 5, 2, 6, 3, 7, 4]
        }
        
        numbering = chord_numbering[mode]
        template = chord_template[mode]
        cformat = chord_type[mode]
        
        chords = []
        for i in range(7):
            i = i + 1
            ind = numbering.index(i)
            chord_type = template[ind]
            chord = self.circlestring[ind]
            chord_format = cformat[ind]
            if chord_format == 'M':
                formatted_chord = chord
            elif chord_format == 'm':
                formatted_chord = chord+'m'
            elif chord_format == 'd':
                formatted_chord = chord+'°'
            
            chords.append((chord_type, chord, chord_format, formatted_chord))
        
        return chords