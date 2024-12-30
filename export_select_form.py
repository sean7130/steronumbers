from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QColorDialog
from ui_export_select import *

class GradientExportSelect(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.mainwindow = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.refresh_gradient_list()
        self.deselect_all_list_items()

        self.ui.gradient_list.itemClicked.connect(self.toggle_check_for_item)

        self.ui.btn_select_all.clicked.connect(self.select_all_list_items)
        self.ui.btn_deselect_all.clicked.connect(self.deselect_all_list_items)
        self.ui.save_button.clicked.connect(self.send_selected_to_save)

    def refresh_gradient_list(self):
        self.ui.gradient_list.clear()
        self.gradient_names = []
        self.names_to_gradient = {}
        for g in self.mainwindow.custom_gradient_objects:
            self.gradient_names.append(g.name)
            self.names_to_gradient[g.name] = g

        self.ui.gradient_list.addItems(self.gradient_names)

    def send_selected_to_save(self):
        send_for_saving = []
        for i in range(self.ui.gradient_list.count()):
            item = self.ui.gradient_list.item(i)
            if item.checkState() == Qt.Checked:
                send_for_saving.append(self.names_to_gradient[item.text()])
        self.mainwindow.save_preset(send_for_saving)

    def select_all_list_items(self):
        self.set_all(True)

    def deselect_all_list_items(self):
        self.set_all(False)

    def set_all(self, selected=True):
        if selected: set_state = Qt.Checked
        else: set_state = Qt.Unchecked

        for i in range(self.ui.gradient_list.count()):
            item = self.ui.gradient_list.item(i)
            item.setCheckState(set_state)

    def toggle_check_for_item(self, item):
        if item.checkState() == Qt.Unchecked:
            item.setCheckState(Qt.Checked)
        else: 
            item.setCheckState(Qt.Unchecked)

