import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.phonon import Phonon

class MainWindow(QtGui.QMainWindow):

    def __init__(self, win_parent=None):
        QtGui.QMainWindow.__init__(self, win_parent)
        self.create_widgets()

    def create_widgets(self):
        # Widgets
        self.label = QtGui.QLabel("ply music player")
        self.fs_button = QtGui.QPushButton("FileSystem", self)
        self.ws_button = QtGui.QPushButton("WebStream", self)

        # Phonon actions
        self.mediaObject = Phonon.MediaObject(self)
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.mediaObject, self.audioOutput)

        # Connect signal
        self.fs_button.clicked.connect(self.on_fs_clicked)
        self.mediaObject.stateChanged.connect(self.handleStateChanged)      
        self.ws_button.clicked.connect(self.on_ws_clicked)

        # Vertical layout (manages the layout automatically)
        v_box = QtGui.QVBoxLayout()
        v_box.addWidget(self.fs_button)
        v_box.addWidget(self.ws_button)

        # Create central widget, add layout and set
        central_widget = QtGui.QWidget()
        central_widget.setLayout(v_box)
        self.setCentralWidget(central_widget)

    def on_fs_clicked(self):
        if self.mediaObject.state() == Phonon.PlayingState:
            self.mediaObject.stop()
        else:
            files = QtGui.QFileDialog.getOpenFileNames(self, self.fs_button.text())
            if files:
                songs = []
                for file in files:
                    songs.append(Phonon.MediaSource(file))
                self.mediaObject.setQueue(songs)
                self.mediaObject.play()
                self.fs_button.setText("FileSystem")

    def handleStateChanged(self, newstate, oldstate):
        if newstate == Phonon.PlayingState:
            self.fs_button.setText("Stop")
        elif newstate == Phonon.StoppedState:
            self.fs_button.setText("FileSystem")
        elif newstate == Phonon.ErrorState:
            source = self.mediaObject.currentSource().fileName()
            print ("ERROR: ", self.mediaObject.errorType())
            print ("ERROR: could not play:", source.toLocal8Bit().data())


    def on_ws_clicked(self):
        if self.mediaObject.state() == Phonon.PlayingState:
            self.mediaObject.stop()
        else:
            song = "http://dr5huvbk6x9di.cloudfront.net/cloudfront_songs/file4.ogg"
            self.mediaObject.setCurrentSource(Phonon.MediaSource(song))
            print (self.mediaObject.currentSource())
            self.mediaObject.play()
            self.ws_button.setText("WebStream")

if __name__ == "__main__":
    ply = QtGui.QApplication(sys.argv)
    ply.setApplicationName("Ply")
    ply.setQuitOnLastWindowClosed(True)
    main_window = MainWindow()
    main_window.show()
    sys.exit(ply.exec_())