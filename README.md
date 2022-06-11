# circleOfFifths
Simple Circle of Fifths application. Works on both Windows and Linux.

Requires:
- PyQt5==5.15.1
- musthe==1.0.0

Can be built into a single executable binary using:
- pyinstaller @ https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz
- pyinstaller-hooks-contrib==2020.9

 `pyinstaller --clean --onefile --windowed --icon=note.ico .\CircleOfFifths.py`
 
 The GUI and resource files are generated from the .ui and .qrc files created with Qt Designer, thus:
 
 `pyuic5.exe .\CircleOfFifths.ui -o circle_ui.py`
 
 `pyrcc5.exe .\CircleOfFifths.qrc -o CircleOfFifths_rc.py`
 
Chords in key of C Major

![Major](/1.png)

A Major - 3 sharps in key

![sharps](/2.png)

Modes

![modes](/3.png)

Notes in common chords

![notes in chord](/4.png)

Adom7 chord shown on Mixolydian scale

![notes in chord](/5.png)

Common chord progressions

![Chord progressions](/6.png)

Click on center to find key from chords

![Find key from chords](/7.png)



