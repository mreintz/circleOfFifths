# circleOfFifths
Simple Circle of Fifths application

Requires:
- PyQt5==5.15.1
- musthe==1.0.0

Can be built into a single executable binary using:
- pyinstaller @ https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz
- pyinstaller-hooks-contrib==2020.9

 pyinstaller --clean --onefile --windowed --icon=note.ico .\CircleOfFifths.py
 
 The GUI and resource files are generated from the .ui and .qrc files created with Qt Designer, thus:
 
 pyuic5.exe .\CircleOfFifths.ui -o circle_ui.py
 pyrcc5.exe .\CircleOfFifths.qrc -o CircleOfFifths_rc.py
 
![Chords in key mode](/screenshot.png)
![Notes in chord mode](/screenshot2.png)
