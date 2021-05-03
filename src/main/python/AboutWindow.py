from __future__ import annotations

import typing

from PySide2 import QtWidgets, QtGui

from ColorParser import *

if typing.TYPE_CHECKING:
    pass
import CONSTANTS
from CONSTANTS import get_resource


class AboutWindow(QtWidgets.QWidget):
    """Window showing basic info, licenses, and version"""
    def __init__(self, main_window):
        """Constructor
        :param main_window:
        """
        super().__init__()
        self.main_window = main_window
        self.setMaximumSize(360, 360)
        self.setMinimumSize(360, 360)
        self.setWindowFlag(QtGui.Qt.Dialog)
        self.about_label = QtWidgets.QLabel()

        # Link settings
        self.about_label.setTextFormat(QtGui.Qt.RichText)
        self.about_label.setTextInteractionFlags(QtGui.Qt.TextBrowserInteraction)
        self.about_label.setOpenExternalLinks(True)

        #Formatting
        self.about_label.setAlignment(QtGui.Qt.AlignCenter)
        self.about_label.setWordWrap(True)
        self.about_label.setText(
            f'<img src="{get_resource("icons/appicons/hires/128.png")}"/>'
            '<p style="font-size: 11pt">'
            '<b>Pepys:</b><br>'
            'A Straightforward Markdown Journal<br>'
            '<a style="text-decoration: none; color: rgb(0,125,225);" '
            '   href="https://lukebriggs.dev">©Luke Briggs</a><br><br><br>'
            '</p>'
            
            '<p style="font-size: 8pt">'
            '<a style="text-decoration: none; color: rgb(0,125,225);" '
            '   href="https://rsms.me/inter/">Inter</a> provided under '
            '<a style="text-decoration: none; color: rgb(0,125,225);" '
            '   href ="https://choosealicense.com/licenses/ofl-1.1/">SIL Open Font License 1.1</a><br>'
            '<a style="text-decoration: none; color: rgb(0,125,225);" '
            '   href = "https://fonts.google.com/specimen/Roboto+Mono">Roboto Mono</a> provided under'
            '<a style="text-decoration: none; color: rgb(0,125,225);" '
            '   href = "https://www.apache.org/licenses/LICENSE-2.0">Apache License 2.0</a>'
            '<br><br><br>'
            f'version {CONSTANTS.version}'
            '</p>'

        )
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.about_label)
        self.setStyleSheet(parse_stylesheet(get_resource("styles.qss"), get_resource("colors.json"), get_resource("config.json")))
        self.setWindowTitle("About")


    def closeEvent(self, event:QtGui.QCloseEvent) -> None:
        self.main_window.setFocusPolicy(QtGui.Qt.StrongFocus)
        self.main_window.setDisabled(False)
