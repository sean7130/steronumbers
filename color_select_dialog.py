import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QColorDialog
from ui_custom_gradient import *

START_COLOR_STR = "Start Color"
END_COLOR_STR = "End Color"

class CustomGradientWindow(Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.mainwindow = parent
        self.setupUi(self)
        self.btn_edit_start_color.clicked.connect(self.determine_start_color)
        self.btn_edit_end_color.clicked.connect(self.determine_end_color)

        self.selected_colors = {}

    def determine_start_color(self):
        self.update_color(self.btn_edit_start_color, self.start_color_label, START_COLOR_STR)

    def determine_end_color(self):
        self.update_color(self.btn_edit_end_color, self.end_color_label, END_COLOR_STR)

    def update_color(self, associated_button=None, associated_label=None, color_type=None):
        """
        args:
            associated_button: QPushButton
            associated_label: QLabel
            color_type: str
        """

        color = QColorDialog.getColor()
        if color.isValid():
            self.selected_colors[color_type] = color
            r = color.red()
            g = color.green()
            b = color.blue()

            style_sheet_str =   "QPushButton{\n"\
                                f"    background-color: rgb({r}, {g}, {b});\n"\
                                "    border-style: outset;\n"\
                                "    border-width: 2px;\n"\
                                "    border-radius: 10px;\n"\
                                "    border-color: black;\n"\
                                "    font: bold 14px;\n"\
                                "    padding: 6px;\n"\
                                "}\n"\
                                "QPushButton:pressed {\n"\
                                "    background-color: rgb(240, 240, 240);\n"\
                                "    border-style: inset;\n"\
                                "}"
            associated_button.setStyleSheet(style_sheet_str)

            associated_label.setText(f"<html><head/><body><p>{color_type}: <span style=\" font-weight:700;\">({r}, {g}, {b})</span></p></body></html>")

            self.mainwindow.report_window_height()


def get_gradient_diaglog(mainwindow):
    ret = CustomGradientWindow(mainwindow)
    return ret