import time
import os
import tinysoundfont
from musthe import Note, Chord, Scale
from PyQt5.QtCore import QFile
import play_sounds_resources

synthfilename = "florestan-piano.sf2"
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
synthfile = os.path.join(__location__, synthfilename)

if not os.path.isfile(synthfile):
    print("Exporting synth file")
    QFile.copy(":/resources/florestan-piano.sf2", synthfile)

synth = tinysoundfont.Synth()
sfid = synth.sfload(synthfile)
synth.program_select(0, sfid, 0, 0)
synth.start()

def play_arpeggio(notes):
    midi_notes = [ n.midi_note() for n in notes ]
    for n in midi_notes:
        synth.noteon(0, n, 100)
        time.sleep(0.3)
        synth.noteoff(0, n)

def play_chord(notes):
    midi_notes = [ n.midi_note() for n in notes ]
    for n in midi_notes:
        synth.noteon(0, n, 100)
    time.sleep(0.5)
    for n in midi_notes:
        synth.noteoff(0, n)

if __name__ == '__main__':
    chord = Chord(Note('C#'), 'min')
    note = Note('C')
    scale = Scale(note, 'major')

    scale_notes = [(note + i) for i in scale.intervals]

    play_chord(chord.notes)
    time.sleep(1)
    play_arpeggio(chord.notes)
    time.sleep(1)
    play_arpeggio(scale_notes)