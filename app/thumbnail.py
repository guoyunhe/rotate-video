from PySide6.QtCore import QTimer, QEventLoop
from PySide6.QtGui import QImage
from PySide6.QtMultimedia import QMediaPlayer, QVideoSink

"""
Generate video thumbnail at 50% position
"""


def thumbnail(url):
    position = 0
    image: QImage = None
    loop = QEventLoop()
    QTimer.singleShot(15000, lambda: loop.exit(1))
    player = QMediaPlayer()
    player.setVideoSink(sink := QVideoSink())
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
