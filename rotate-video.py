#!/usr/bin/python3

import sys
import gettext
from PySide6.QtWidgets import QApplication
from app.mainwindow import MainWindow

binName = 'rotate-video'

if __name__ == "__main__":
    gettext.bindtextdomain(binName)

    app = QApplication(sys.argv)

    widget = MainWindow()
    widget.show()

    status = app.exec()
    sys.exit(status)
