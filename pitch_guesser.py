# READ ME
# pyqt uses .ui files to create the GUI. To edit the GUI, open the .ui file in Qt Designer and edit it there.
# For this to be possible, I need to install pyqt5-tools. To do this, I need to install pyqt5 first.
#, QPushButton, QVBoxLayout, QLabel, QComboBox, QGridLayout, QGroupBox, QRadioButton, QHBoxLayout, QSlider, QLCDNumber

#from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
#from PySide6.QtMultimedia import QMediaPlayer, QMediaContent
#from PySide6.QtCore import QUrl

# The QMediaPlayer class has all kinds of properties that you may know from video players: audioAvailable, duration, position, volume and a few others.

#Include pyqt5 libraries

import sys
import random
from PySide6 import QtWidgets, QtCore, QtMultimedia

class PitchPlayer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("=====================================DO SOMETHING RETARD+++++++++")
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        # Size the window

        self.helloButton = QtWidgets.QPushButton("Magic!")
        self.playButton = QtWidgets.QPushButton("Play Audio")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.helloButton)
        self.layout.addWidget(self.playButton)

        self.helloButton.clicked.connect(self.magic)
        self.playButton.clicked.connect(self.play_media)

        self.player = QtMultimedia.QMediaPlayer(self)
        self.player.setSource(QtCore.QUrl.fromLocalFile("music.wav"))
        self.player.durationChanged.connect(self.update_duration_label)

        # Connect to error and status signals
        self.player.errorOccurred.connect(self.handle_media_error)
        self.player.mediaStatusChanged.connect(self.handle_media_status)

    def play_media(self):
        self.player.play()
        self.update_duration_label()

    def update_duration_label(self):
        duration_ms = self.player.duration()
        minutes, milliseconds = divmod(duration_ms, 60000)
        seconds = milliseconds // 1000
        self.helloButton.setText(f"Duration: {minutes:02d}:{seconds:02d}")

    @QtCore.Slot()
    def magic(self):
        self.helloButton.setText(random.choice(self.hello))
        self.play_media()

    def handle_media_error(self, error, errorString):
        print(f"Media error: {error}, {errorString}")
        QtWidgets.QMessageBox.critical(self, "Media Error", f"Error playing media: {errorString}")

    def handle_media_status(self, status):
        print(f"Media status changed: {status}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PitchPlayer()
    window.show()
    sys.exit(app.exec())



def build_note_array(low_C):
    lowest_note = {"C1": 16.35}
    letters = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    notes = {}
    for half_step in letters:
        for octave in range(0, 9):
            note = half_step + str(octave)
            notes[note] = lowest_note["C1"] * (2 ** (octave + (letters.index(half_step) / 12)))
    return notes


