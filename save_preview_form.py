from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QColorDialog, QMessageBox
from ui_save_image_preview import *
from shutil import copy

class SavePreview(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.mainwindow = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.top_level_widgets = [
            self.ui.groupBox,
            self.ui.vframe_preview,
            self.ui.close_button,
            self.ui.save_button
        ]

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
            msg = QMessageBox()
            msg.setWindowTitle("Save File")
            msg.setStandardButtons(QMessageBox.Ok)
            try:
                copy(self.save_preview_str, path)
                msg.setText("Save Sucessful!")
                msg.setIcon(QMessageBox.Information)
                msg.exec()
                # upon save success, close window
                self.close()

            except PermissionError as e:
                print(f"Permission denied: {e}")
                msg.setText(f"Permission denied: {e}")
                msg.setIcon(QMessageBox.Critical)
                msg.exec()
            except OSError as e:
                print(f"OS error: {e}")
                msg.setText(f"OS error: {e}")
                msg.setIcon(QMessageBox.Critical)
                msg.exec()


    def select_custom_bg(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.update_settings((color.red(), color.green(), color.blue()))
            # deselect everything else in the list
            for r in self.radio_buttons:
                print(f"deselecting {r}")
                r.setAutoExclusive(False)
                r.setChecked(False)
                r.setAutoExclusive(True)

    def update_to_white(self):
        self.update_settings((255,255,255))
        # note QRadioButton by design will deselect others in group upon press. 
        # therefore, no futher logic required for handling

    def update_to_black(self):
        self.update_settings((0, 0, 0))

    def update_to_default(self):
        self.update_settings((240, 240, 240))

    def update_settings(self, color):
        self.mainwindow.generate_save_preview(self.save_preview_str, color)
        self.ui.img_preview_label.setPixmap(self.save_preview_str)

    def apply_stylesheet(self, stylesheet):
        for w in self.top_level_widgets:
            w.setStyleSheet(stylesheet)
        
