from __future__ import annotations

import typing

from PySide2 import QtWidgets, QtGui

from CONSTANTS import get_resource
from ColorParser import *

if typing.TYPE_CHECKING:
    pass


class ExportWindow(QtWidgets.QWidget):
    """Window for selecting export options"""

    output_formats = {
        "Word Document": "docx",
        "EBook": "epub",
        "HTML": "html",
        "PDF": "pdf",
        "Latex": "latex",
        "OpenOffice Text Document": "odt",
        "Plain Text": "plain",
        "PowerPoint Slide Show": "pptx",
        "Rich Text Format": "rtf",
        "reStructuredText": "rst",
    }

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setMaximumSize(640, 240)
        self.setMinimumSize(640, 240)
        self.setWindowFlag(QtGui.Qt.Dialog)
        self.setLayout(QtWidgets.QGridLayout())

        self.export_options = QtWidgets.QComboBox()
        self.export_options.setFixedWidth(240)

        for output_format in sorted(self.output_formats.keys(), key=str.lower):
            self.export_options.addItem(output_format)

        self.setLayout(QtWidgets.QVBoxLayout())

        self.export_label = QtWidgets.QLabel("Export Format")
        self.layout().addWidget(self.export_label, 0, 0)
        self.layout().addWidget(self.export_options,0, 1, 1, 5)

        self.export_button = QtWidgets.QPushButton("Export")
        self.layout().addWidget(self.export_button)

        self.setStyleSheet(parse_stylesheet(get_resource("styles.qss"), get_resource("colors.json"), get_resource("config.json")))

        self.setWindowTitle("Export")


    def closeEvent(self, event:QtGui.QCloseEvent) -> None:
        # Re-enable main window
        self.main_window.setFocusPolicy(QtGui.Qt.StrongFocus)
        self.main_window.setDisabled(False)
