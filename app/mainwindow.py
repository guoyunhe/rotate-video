from PySide6.QtCore import QUrl
from PySide6.QtCore import QTimer, QEventLoop
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QMainWindow,
    QProgressBar,
    QToolBar,
    QToolButton,
    QVBoxLayout,
    QWidget,
)
from gettext import gettext as _
from PySide6.QtGui import QImage
from PySide6.QtMultimedia import QMediaPlayer, QVideoSink


class MainWindow(QMainWindow):
    def __init__(self,  parent: QWidget = None):
        super().__init__(parent)

        self.setWindowTitle(_('Rotate Video'))

        toolbar = QToolBar(self)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        open_video_button = QToolButton(self)
        open_video_button.setText(_('&Open video...'))
        open_video_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        open_video_button.setIcon(QIcon.fromTheme('document-open'))
        open_video_button.clicked.connect(self.open_file)
        toolbar.addWidget(open_video_button)

        toolbar.addSeparator()

        rotate_left_button = QToolButton(self)
        rotate_left_button.setText(_('Rotate &left'))
        rotate_left_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        rotate_left_button.setIcon(QIcon.fromTheme('object-rotate-left'))
        rotate_left_button.clicked.connect(self.rotate_left)
        toolbar.addWidget(rotate_left_button)

        rotate_right_button = QToolButton(self)
        rotate_right_button.setText(_('Rotate &right'))
        rotate_right_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        rotate_right_button.setIcon(QIcon.fromTheme('object-rotate-right'))
        rotate_right_button.clicked.connect(self.rotate_right)
        toolbar.addWidget(rotate_right_button)

        toolbar.addSeparator()

        convert_save_button = QToolButton(self)
        convert_save_button.setText(_('&Save'))
        convert_save_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        convert_save_button.setIcon(QIcon.fromTheme('document-save'))
        toolbar.addWidget(convert_save_button)

        convert_saveas_button = QToolButton(self)
        convert_saveas_button.setText(_('Save &as...'))
        convert_saveas_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        convert_saveas_button.setIcon(QIcon.fromTheme('document-save-as'))
        toolbar.addWidget(convert_saveas_button)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(self)
        central_widget.setLayout(main_layout)

        self.image_viewer = QLabel(self)
        main_layout.addWidget(self.image_viewer)

        progress_bar = QProgressBar(self)
        progress_bar.setValue(20)
        main_layout.addWidget(progress_bar)

    def open_file(self):
        video, pattern = QFileDialog.getOpenFileName(self, _(
            'Open video'), '/home/guo', _('Video Files (*.avi *.mkv *.mp4 *.webm)'))
        self.video_file_path = video
        self.image = self.thumbnail(QUrl.fromLocalFile(video))
        if (self.image):
            self.image_viewer.setPixmap(self.image)

    def thumbnail(self, url):
        position = 0
        image: QImage = None
        loop = QEventLoop(self)
        QTimer.singleShot(15000, lambda: loop.exit(1))
        player = QMediaPlayer(self)
        player.setVideoSink(sink := QVideoSink(self))
        player.setSource(url)

        def handle_status(status):
            nonlocal position
            print('status changed:', status.name)
            # if status == QMediaPlayer.MediaStatus.LoadedMedia:
            if status == QMediaPlayer.MediaStatus.BufferedMedia:
                player.setPosition(position := player.duration() // 2)
                print('set position:', player.position())

        def handle_frame(frame):
            nonlocal image
            print('frame changed:', frame.startTime() // 1000)
            if (start := frame.startTime() // 1000) and start >= position:
                sink.videoFrameChanged.disconnect()
                image = frame.toImage()
                print('save: exit')
                loop.exit()
        player.mediaStatusChanged.connect(handle_status)
        sink.videoFrameChanged.connect(handle_frame)
        player.durationChanged.connect(
            lambda value: print('duration changed:', value))
        player.play()
        if loop.exec() == 1:
            print('ERROR: process timed out')
        return image

    def rotate_left(self):
        print('left')

    def rotate_right(self):
        print('right')
