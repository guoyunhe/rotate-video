from socket import socket
from PySide6.QtWidgets import (
    QMainWindow,
    QProgressBar,
    QToolBar,
    QToolButton,
    QVBoxLayout,
    QWidget,
    QSpacerItem,
    QSizePolicy
)
from PySide6.QtGui import (Qt, QIcon)
from gettext import gettext as _


class MainWindow(QMainWindow):
    def __init__(self,  parent: QWidget = None):
        super().__init__(parent)

        self.setWindowTitle(_('Rotate Video'))

        toolbar = QToolBar(self)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        open_file_button = QToolButton(self)
        open_file_button.setText(_('&Open file...'))
        open_file_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        open_file_button.setIcon(QIcon.fromTheme('document-open'))
        toolbar.addWidget(open_file_button)

        toolbar.addSeparator()

        rotate_left_button = QToolButton(self)
        rotate_left_button.setText(_('Rotate &left'))
        rotate_left_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        rotate_left_button.setIcon(QIcon.fromTheme('object-rotate-left'))
        toolbar.addWidget(rotate_left_button)

        rotate_right_button = QToolButton(self)
        rotate_right_button.setText(_('Rotate &right'))
        rotate_right_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        rotate_right_button.setIcon(QIcon.fromTheme('object-rotate-right'))
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

        progress_bar = QProgressBar(self)
        progress_bar.setValue(20)
        main_layout.addWidget(progress_bar)
