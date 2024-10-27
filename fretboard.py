from musthe import *
import pandas as pd

class Fretboard():
    def __init__(self, tuning):

        self.enharmonics = [
            ['C',  'C',  'B#',  'Dbb'],
            ['C#', 'Db'              ],
            ['D',  'D',  'C##', 'Ebb'],
            ['D#', 'Eb',        'Fbb'],
            ['E',  'E',  'D##', 'Fb' ],
            ['F',  'F',  'E#',  'Gbb'],
            ['F#', 'Gb', 'E##'       ],
            ['G',  'G',  'F##', 'Abb'],
            ['G#', 'Ab'              ],
            ['A',  'A',  'G##', 'Bbb'],
            ['A#', 'Bb',        'Cbb'],
            ['B',  'B',  'A##', 'Cb' ],
        ]

        # Reverse tuning for "top-down view"
        self.tuning = tuning[::-1]

        # Contains all the possible notes on the fretboard with a certain tuning
        self.all_the_notes = {}
        string = 1

        # For each tuning peg, build the fretboard
        for peg in self.tuning:
            index = 0

            # Check where on the enharmonic list we begin our one-string chromatic scale
            for e in self.enharmonics:
                if peg in self.enharmonics[index]:
                    # We have found our index and can build our chromatic scale
                    all_the_notes = self.enharmonics[index:] + self.enharmonics[:index]
                    all_the_notes = all_the_notes + all_the_notes # 23 frets
                    all_the_notes.append(all_the_notes[0]) # 24 frets
                    self.all_the_notes[string] = all_the_notes
                    break
                else:
                    index = index + 1
            string = string + 1

    def build(self, **kwargs):
        if kwargs:
            if 'chord' in kwargs:
                self.chord = kwargs['chord']
                self.notes = [ str(n) for n in self.chord.notes ]
                self.intervals = self.chord.recipes[self.chord.chord_type]
                if 'P8' in self.intervals:
                    index = self.intervals.index('P8')
                    del self.notes[index]
                    del self.intervals[index]
            elif 'scale' in kwargs:
                self.scale = kwargs['scale']
                self.notes = [ str(n) for n in self.scale.notes ]
                self.intervals = [ str(i) for i in self.scale.intervals ]
            else:
                print("You must supply at least one chord= or scale= keyword argument. Reverting to C major.")
                self.scale = Scale(Note('C'), 'major')
                self.notes = [ str(n) for n in self.scale.notes ]
                self.intervals = [ str(i) for i in self.scale.intervals ]
            if 'frets' in kwargs:
                self.frets = kwargs['frets']
                if max(self.frets) > 24 or min(self.frets) < 0:
                    print("Frets must be between 0 and 24")
                    self.frets = (0, 24)
            else:
                self.frets = (0, 24)

        """Place all the submitted notes on the fretboard."""
        notes_grid = []
        intervals_grid = []

        # Go through all the possible enharmonic notes on each string
        for string in self.all_the_notes.keys():
            notes_row = []
            intervals_row = []

            # For each "slot" on the string, check if we find the desired note
            for slot in self.all_the_notes[string]:
                match = False
                for n in self.notes:
                    if n in slot:
                        notes_row.append(n)
                        intervals_row.append(self.intervals[ self.notes.index(n) ])
                        match = True
                if not match:
                    notes_row.append("")
                    intervals_row.append("")
            notes_grid.append(notes_row)
            intervals_grid.append(intervals_row)
            if self.frets == (0, 24):
                self.notes_grid = notes_grid
                self.intervals_grid = intervals_grid
            else:
                df_n = pd.DataFrame(notes_grid)
                df_i = pd.DataFrame(intervals_grid)
                fret_slice = range(self.frets[0], self.frets[1]+1)
                self.notes_grid = df_n[ fret_slice ].values.tolist()
                self.intervals_grid = df_i[ fret_slice ].values.tolist()
        return self.notes_grid, self.intervals_grid

    def printPlain(self):
        def plainprint(grid):
            for row in grid:
                for note in row:
                    print(note.center(5), end="")
                print()
            for fret in range(self.frets[0], self.frets[1]+1):
                if fret == 0:
                    print("N".center(5), end="")
                else:
                    print(str(fret).center(5), end="")
            print("\n")

        def header():
            try:
                print(f'{str(self.chord.notes[0])} {self.chord.chord_type} chord')
            except AttributeError:
                try:
                    print(f'{str(self.scale.root)} {self.scale.name} scale')
                except AttributeError:
                    pass

        header()
        plainprint(self.notes_grid)

        header()
        plainprint(self.intervals_grid)
