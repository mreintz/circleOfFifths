from musthe import *

def translate(string):
    string=string.replace('b', '♭')
    string=string.replace('#', '♯')
    return string

def majmin(chordno, chord):
    if '°' in chordno:
        return chord+'°'
    elif chordno.islower():
        return chord+'m'
    else:
        return chord

translateNote = {
    'B#': 'C',
    'E#': 'F',
    'Fb': 'E',
    'Cb': 'B',
    'Ebb': 'D',
    'Bbb': 'A'
}

def readable(note):
    return str(note.letter)+note.accidental

def progression(key, pattern, mode):
    pat = []
    chords = []

    if mode == 'Major':
        s = Scale(key, 'major')
    else:
        s = Scale(key, 'natural_minor')
        
    for p in pattern[0]:
        note = readable(s[p])

        pat.append(pattern[1][p])
        chords.append(majmin(pattern[1][p], translate(translateNote.get(note, note))))

    return (pat, chords)