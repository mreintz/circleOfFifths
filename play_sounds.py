import time
import tinysoundfont
from musthe import Note, Chord, Scale

synth = tinysoundfont.Synth()
sfid = synth.sfload("florestan-piano.sf2")
synth.program_select(0, sfid, 0, 0)
synth.start()

def play_arpeggio(notes):
    midi_notes = [ n.midi_note() for n in notes ]
    for n in midi_notes:
        synth.noteon(0, n, 100)
        time.sleep(0.5)
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