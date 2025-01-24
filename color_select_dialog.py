import sys, os
from random import randint
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QColorDialog
from ui_custom_gradient import *

START_COLOR_STR = "Start Color"
END_COLOR_STR = "End Color"

class GradientCallable():
    def __init__(self, start_color=None, end_color=None):
        if start_color and end_color:
            self.__setup_gradient_object(start_color, end_color)
        else:
            self.grad_function = lambda x: (0, 0, 0)
            self.dump_data = lambda: ""

    #TODO: remove & replace this one later
    def __setup_gradient_object(self, start_color, end_color):
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

            # This will be set upon accept (within add_new_gradient of mainwindow)
            # Alternatively, restore_from_file_data will set this field too
            self.name = None 

            self.grad_function = self.__grad_function
            self.dump_data = self.__dump_data

    def __str__(self):
        return f"{self.start_rgb}->{[self.end_color.red(), self.end_color.green(), self.end_color.blue()]}"

    def __grad_function(self, num):
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

    def __dump_data(self):
        ret = f"{self.name}, {str(self.start_rgb)[1:-1]}, {self.end_color.red()}, {self.end_color.green()}, {self.end_color.blue()}"
        return ret

    #TODO: make better interfaces for this
    def save_one_to_file(self, filename):
        fd = open(filename, "w")
        fd.write(self.dump_data)
        fd.close()

    def restore_from_file_data(self, data):
        splitted = data.split(",")
        formatted_data = [e.strip() for e in splitted]
        self.__setup_gradient_object(QColor(int(formatted_data[1]),
                                            int(formatted_data[2]),
                                            int(formatted_data[3])),
                                     QColor(int(formatted_data[4]),
                                            int(formatted_data[5]),
                                            int(formatted_data[6]))
                                     )

        self.name = formatted_data[0]


class CustomGradientWindow(Ui_Dialog):
    def __init__(self, parent=None, s_color=QColor(170,255,0), t_color=QColor(85,170,127)):
        super().__init__()
        self.mainwindow = parent
        self.setupUi(self)

        # =========================== styling =============================
        # self.Dialog.setStyleSheet("background-color : rgb(245, 245, 245)")
        self.top_level_widgets = [
            self.buttonBox,
            self.line_edit_save_gradient,
            self.line_preview,
            self.groupBox
        ]
        # self.apply_stylesheet will be called by parent

        # =============================== Setup =============================== 
        self.selected_colors = {START_COLOR_STR: s_color, END_COLOR_STR: t_color}
        self.update_color(self.btn_edit_start_color, self.start_color_label, START_COLOR_STR, manual_color=s_color)
        self.update_color(self.btn_edit_end_color, self.end_color_label, END_COLOR_STR, manual_color=t_color)

        # ============================== Buttons ============================== 
        self.btn_edit_start_color.clicked.connect(self.determine_start_color)
        self.btn_edit_end_color.clicked.connect(self.determine_end_color)

    def accept(self):
        self.mainwindow.add_new_gradient(self.pending_gradient, self.line_edit_save_gradient.text())
        gradient_count = self.mainwindow.ui.gradient_select.count()
        if gradient_count != len(self.mainwindow.collection_gradients): 
            print(f"WARN: grad combobox count mismatch with collection_gradients: {gradient_count}!={len(self.mainwindow.collection_gradients)}")
        self.mainwindow.ui.gradient_select.setCurrentIndex(gradient_count-1)

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

        self.mainwindow.collection_gradients[self.mainwindow.last_unsaved_custom_slot] = custom_grad_function
        self.pending_gradient = g

        # update the stylesheet based on the colors have selected via help from the mainwindow (parent) window
        self.apply_stylesheet(self.request_custom_stylesheet(
            self.selected_colors[START_COLOR_STR],
            self.selected_colors[END_COLOR_STR])
                                  )
        return custom_grad_function

    def update_color(self, associated_button=None, associated_label=None, color_type=None, manual_color=None):
        """
        args:
            associated_button: QPushButton
            associated_label: QLabel
            color_type: str
        """

        if manual_color:
            color = manual_color
        else:
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

            self.generate_and_set_preview()
            
            # special case if the gradent seelect combobox is selected on "last custom", then update
            if self.mainwindow.ui.gradient_select.currentIndex() == self.mainwindow.last_unsaved_custom_slot:
                self.mainwindow.update_gradient_settings(self.mainwindow.last_unsaved_custom_slot)


    def request_custom_stylesheet(self, s_color, t_color):
        return self.mainwindow.provide_one_time_stylesheet(s_color, t_color)

    def apply_stylesheet(self, stylesheet):
        for w in self.top_level_widgets:
            w.setStyleSheet(stylesheet)
            

def get_gradient_diaglog(mainwindow, s=None, t=None):
    if s and t:
        ret = CustomGradientWindow(mainwindow, s_color=s, t_color=t)
    else:
        # radnom color generation
        s = [randint(0,255) for _ in range(3)]
        t = [randint(0,255) for _ in range(3)]
        s[randint(0, 2)] = 255
        t[randint(0, 2)] = 255
        s_color = QColor(s[0], s[1], s[2])
        t_color = QColor(t[0], t[1], t[2])
        ret = CustomGradientWindow(mainwindow, s_color=s_color, t_color=t_color)
    return ret
