from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QColorDialog
from ui_save_image_preview import *
from shutil import copy

class SavePreview(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.mainwindow = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.save_preview_str = "preview_save.png"

        self.radio_buttons = [self.ui.radio_white, 
                              self.ui.radio_black, 
                              self.ui.radio_default
                              ]

        self.ui.radio_white.clicked.connect(self.update_to_white)
        self.ui.radio_black.clicked.connect(self.update_to_black)
        self.ui.radio_default.clicked.connect(self.update_to_default)

        self.ui.custom_color_button.clicked.connect(self.select_custom_bg)
        self.ui.save_button.clicked.connect(self.save_file)
        self.ui.close_button.clicked.connect(self.close)
        self.update_to_default()

    def save_file(self):
        path, _ = QFileDialog.getSaveFileName(
            self,                   
            "Save file",            
            "",                     
            "Portable Network Graphics (*.png);;All Files (*)"
        )

        if path:
            copy(self.save_preview_str, path)

    def select_custom_bg(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.update_settings((color.red(), color.green(), color.blue()))

    def update_to_white(self):
        self.update_settings((255,255,255))

    def update_to_black(self):
        self.update_settings((0, 0, 0))

    def update_to_default(self):
        self.update_settings((240, 240, 240))

    # function might not be needed
    # def update_state(checked_idx):
    #     for i in range(len(self.radio_buttons)):
    #         if i == checked_idx:
    #             self.radio_buttons[i].setDown(True)
    #         else:
    #             self.radio_buttons[i].setDown(False)


    def update_settings(self, color):
        self.mainwindow.generate_save_preview(self.save_preview_str, color)
        self.ui.img_preview_label.setPixmap(self.save_preview_str)
