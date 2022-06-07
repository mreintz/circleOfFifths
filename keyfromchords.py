import circle
from musthe import *

keys0 = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Db', 'Ab', 'Eb', 'Bb', 'F']
keys0_sharp = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'F'] 
keys0x2 = keys0 + keys0
keys0_sx2 = keys0_sharp + keys0_sharp

keys_chords = []
for key in keys0:
    chords = []
    c = circle.CircleOfFifths(Note(key))
    for chord in c.chords():
        chords.append(chord[3])
    keys_chords.append(chords)

def findKeyFromChords(mychords, *args):
    if args:
        majmin = args[0]
    else:
        majmin = False
    
    sharpchords = mychords.copy()
    flatchords = mychords.copy()
    i = 0 

    for c in sharpchords:
        major = c.split('m')
        if len(major) == 2:
            minor = 'm'
        else:
            minor = ''

        try:
            if major[0] == 'Gb':
                major = 'F#'+minor
            else:
                sharp = keys0_sharp[keys0x2.index(major[0])]+minor
            sharpchords[i] = sharp    
        except ValueError:
            pass
        finally:
            i = i + 1

    i = 0
    for c in flatchords:
        major = c.split('m')
        if len(major) == 2:
            minor = 'm'
        else:
            minor = ''

        try:
            if major[0] == 'F#':
                flat = 'Gb'+minor
            else:
                flat = keys0[keys0_sx2.index(major[0])]+minor
            flatchords[i] = flat    
        except ValueError:
            pass
        finally:
            i = i + 1        

    possible_keys = []
    i = 0 
    for keys in keys_chords:
        if all(elem in keys_chords[i] for elem in flatchords) or all(elem in keys_chords[i] for elem in sharpchords):
            major = keys_chords[i][0]
            try:
                minor = keys0x2[keys0_sx2.index(major) + 3]
            except ValueError:
                minor = keys0x2[keys0x2.index(major) + 3]                

            if majmin == 'minor':
                possible_keys.append(minor+'m')
            elif majmin == 'major':
                possible_keys.append(major)
            else:
                possible_keys.append(major)
                possible_keys.append(minor+'m')

        i = i + 1
        
    return possible_keys