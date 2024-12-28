import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QColorDialog
from ui_custom_gradient import *

START_COLOR_STR = "Start Color"
END_COLOR_STR = "End Color"

class GradientCallable():
    def __init__(self, start_color, end_color):
        self.start_color = start_color
        self.start_rgb = [start_color.red(), start_color.green(), start_color.blue()]

        self.end_color = end_color

        # determines the color differences between the RGB channel
        self.deltas = [
            end_color.red() - start_color.red(),
            end_color.green() - start_color.green(),
            end_color.blue() - start_color.blue()
        ]

        # using delta, now determine increments, which by design of how gradient functions work,
        # they will have a total of 10 increment, therefore they are each delta / 10 (or 9,
        # depending on if we want to push close to the end color or not)
        self.increments = [e/9 for e in self.deltas]

    def grad_function(self, num):
        """
        args: 
            num (int):  a range from 0-9, where 0 is closest to self.start_color,
                        and 9 is closest to end color:
        """
        # one line solution: but may be slower
        # tuple([int(self.start_rgb[i]+self.increments[i]*num) for i in range(3)])
        return (int(self.start_rgb[0]+self.increments[0]*num),
                int(self.start_rgb[1]+self.increments[1]*num),
                int(self.start_rgb[2]+self.increments[2]*num))


class CustomGradientWindow(Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.mainwindow = parent
        self.setupUi(self)
        self.btn_edit_start_color.clicked.connect(self.determine_start_color)
        self.btn_edit_end_color.clicked.connect(self.determine_end_color)

        self.selected_colors = {START_COLOR_STR: QColor(170,255,0), END_COLOR_STR: QColor(85,170,127)}

        self.generate_and_set_preview() # for the init colors

    def determine_start_color(self):
        self.update_color(self.btn_edit_start_color, self.start_color_label, START_COLOR_STR)

    def determine_end_color(self):
        self.update_color(self.btn_edit_end_color, self.end_color_label, END_COLOR_STR)

    def generate_and_set_preview(self):
        g = GradientCallable(self.selected_colors[START_COLOR_STR], self.selected_colors[END_COLOR_STR])
        custom_grad_function = g.grad_function
        self.mainwindow.generate_one_line_gradient_preview(custom_grad_function)

        # by now we assume the image is generated, we will look for 'gradient_preview.png'
        self.line_preview.setPixmap("gradient_preview.png")
        return custom_grad_function

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

            user_custom_grad = self.generate_and_set_preview()

            # TODO: next two lines need to be streamlined in the future to support multiple custom gradients
            self.mainwindow.custom_gradient_functions.append(user_custom_grad)
            self.mainwindow.collection_gradients[-1] = user_custom_grad

def get_gradient_diaglog(mainwindow):
    ret = CustomGradientWindow(mainwindow)
    return ret