# This Python file uses the following encoding: utf-8
import sys
import time

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

import stero_numbers as sn

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.horizontalSlider_2.valueChanged.connect(self.slider_value_changed)
    #     self.ui.pushButton.setText("this is my text")
    #     self.ui.pushButton.setText("this is overwriting")

    #     self.imageChair = True
        # self.ui.pushButton_3.clicked.connect(self.change_val)
        
        # ======================= spinboxes and slider =======================
        self.spinbox_slider_setup_boilerplate()

        # the font_spacing is the most import one, it can be used to
        # automatically determine the value of col and offset values,
        # so we connect it to a wrapper function
        self.setup_spinbox_slider_relation(self.ui.slide_font_spacing,
                                           self.ui.spin_font_spacing,
                                           0, 20, 10
                                           )
        self.ui.slide_font_spacing.valueChanged.connect(self.slide_font_spacing_wrap)
        self.ui.spin_font_spacing.valueChanged.connect(self.spin_font_spacing_wrap)

        self.setup_spinbox_slider_relation(self.ui.slide_column_spacing ,
                                           self.ui.spin_column_spacing,
                                           50, 150, 97
                                           )

        self.setup_spinbox_slider_relation(self.ui.slide_row_spacing,
                                           self.ui.spin_row_spacing,
                                           0, 50, 25
                                           )

        self.setup_spinbox_slider_relation(self.ui.slide_offset,
                                           self.ui.spin_offset,
                                           0, 10, 1
                                           )

        # =================== height and width spinboxes ===================
        self.ui.width_adjust_spinbox.setMinimum(600)
        self.ui.height_adjust_spinbox.setMinimum(400)
        self.ui.width_adjust_spinbox.setMaximum(3000)
        self.ui.height_adjust_spinbox.setMaximum(3000)
        self.ui.width_adjust_spinbox.valueChanged.connect(self.update_label_and_preview_image_size_manually)
        self.ui.height_adjust_spinbox.valueChanged.connect(self.update_label_and_preview_image_size_manually)

        self.collection_width_height_spinbox = [self.ui.width_adjust_spinbox,
                                                self.ui.height_adjust_spinbox,
                                                self.ui.height_label,
                                                self.ui.width_label]

        # =========================== checkboxes =========================== 
        self.ui.check_auto_column.stateChanged.connect(self.check_auto_col)
        self.ui.check_auto_offset.stateChanged.connect(self.check_auto_offset)
        self.ui.check_auto_size.stateChanged.connect(self.check_auto_resize)

        # ========================== number source ========================== 
        self.ui.source_numbers_text.textChanged.connect(self.src_num_changed)
        self.ui.import_btn.clicked.connect(self.import_via_builtin_file_select)

        
        self.ui.save_btn.clicked.connect(self.report_window_height) #TODO remove later

        # ======================== gradient combo box =======================
        self.ui.gradient_select.currentIndexChanged.connect(self.update_gradient_settings)
        self.collection_gradients = [sn.grad_none, 
                                     sn.grad_pink_to_green,
                                     sn.grad_pink_to_green]

        # =========================== preview_img =========================== 
        self.reload_image()

    # def cycleImg100(self):
    #     for i in range(10):
    #         print(f"{i}")
    #         time.sleep(0.1)
    #         self.cycleImg()

    # def cycleImg(self):
    #     if self.imageChair:
    #         self.ui.label.setPixmap("2.jpg")
    #     else: 
    #         self.ui.label.setPixmap("science.png")
    #     self.imageChair = not(self.imageChair)

    def spinbox_slider_setup_boilerplate(self):
        self._spinbox_to_slider = dict()
        self._slider_to_spinbox = dict()
        self._slider_increment_mult = dict()
        self._spinbox_last_value = dict()
        # self._slider_data = dict()
        self.update_lock = False

    def setup_spinbox_slider_relation(self,
                                      slider, spinbox, 
                                      min_val, max_val, 
                                      default_val,
                                      increment_mult=100):
        # relationship dict
        self._spinbox_to_slider[spinbox] = slider
        self._slider_to_spinbox[slider] = spinbox 
        self._slider_increment_mult[slider] = increment_mult
        self._slider_increment_mult[spinbox] = increment_mult

        slider.setMinimum(min_val * increment_mult)
        slider.setMaximum(max_val * increment_mult)
        spinbox.setMinimum(min_val)
        spinbox.setMaximum(max_val)
        # slider.setSingleStep(0.1) # 0.1 value doesn't work
        # emprically, seem like the smallest increment is 1
        slider.setValue(default_val * increment_mult)
        spinbox.setValue(default_val)
        self._spinbox_last_value[spinbox] = default_val

        slider.valueChanged.connect(self.update_slider_value_to_spinbox)
        spinbox.valueChanged.connect(self.update_spinbox_value_to_slider)

    def update_slider_value_to_spinbox(self, value):
        # print(f"value: {value}")
        if not self.update_lock:
            self.update_lock = True
            slider = self.sender()
            precision = self._slider_increment_mult[slider]
            corr_spinbox = self._slider_to_spinbox[slider]
            corr_spinbox.setValue(value/precision)
            # TODO, put this entire function into a wrapper that calls
            # the reload function seperately (this is so offset doesn't 
            # need to call double reloads, but if the performance isn't
            # affected this can also be ingored)
            self.reload_image()
            self.update_lock = False

    def update_spinbox_value_to_slider(self, value):
        # print(f"value: {value}")
        if not self.update_lock:
            self.update_lock = True
            spinbox = self.sender()
            precision = self._slider_increment_mult[spinbox]
            corr_slider = self._spinbox_to_slider[spinbox]
            corr_slider.setValue(value*precision)
            self.reload_image()
            self.update_lock = False

        

    def live_update_col_and_offset_if_needed(self):
        if self.ui.check_auto_column.isChecked() or self.ui.check_auto_offset.isChecked():
            if self.ui.check_auto_column.isChecked():
                self.simutanious_update_spin_slide_combo(self.ui.spin_column_spacing, 
                                                         self.get_col_auto_value())
            if self.ui.check_auto_offset.isChecked():
                self.simutanious_update_spin_slide_combo(self.ui.spin_offset,
                                                         self.get_offset_auto_value())
            self.reload_image()

    def slide_font_spacing_wrap(self, value):
        self.update_slider_value_to_spinbox(value)
        self.live_update_col_and_offset_if_needed()

    def spin_font_spacing_wrap(self, value):
        self.update_spinbox_value_to_slider(value)
        self.live_update_col_and_offset_if_needed()

    def get_font_spacing(self):
        return self.ui.spin_font_spacing.value()

    def get_col_spacing(self):
        return self.ui.spin_column_spacing.value()

    def get_row_spacing(self):
        return self.ui.spin_row_spacing.value()

    def get_offset(self):
        return self.ui.spin_offset.value()

    def get_col_auto_value(self):
        return self.get_font_spacing()*10 - 3

    def get_offset_auto_value(self):
        return max(self.get_font_spacing()//10, 1) # shouldn't be 0 or else flat

    def simutanious_update_spin_slide_combo(self, spinbox, spinbox_value):
        spinbox.setValue(spinbox_value)
        if self.update_lock:
            slider = self._spinbox_to_slider[spinbox]
            multi = self._slider_increment_mult[slider]
            slider.setValue(spinbox_value * multi)
            

    def check_auto_col(self, state):
        if state == 2:
            new_state = False
            self._spinbox_last_value[self.ui.spin_column_spacing] = self.get_col_spacing()
            # once spinbox value is changed, the slider value would not
            # sync to the slidebox counterpart (self.update_lock is on)
            # need manually change or TODO: determine a better way to do
            # this. Currenlty a override function is used to get around.
            self.simutanious_update_spin_slide_combo(self.ui.spin_column_spacing, 
                                                     self.get_col_auto_value())
        else: 
            new_state = True
            # lock is not on, so just changing spinbox value will do, no
            # further action required. TODO: see if this is desired, or
            # should setValue be replaced by 
            # simutanious_update_spin_slide_combo()
            value_before = self._spinbox_last_value[self.ui.spin_column_spacing]
            self.ui.spin_column_spacing.setValue(value_before)

        self.ui.spin_column_spacing.setEnabled(new_state)
        self.ui.slide_column_spacing.setEnabled(new_state)


    def check_auto_offset(self, state):
        if state == 2:
            new_state = False
            self._spinbox_last_value[self.ui.spin_offset] = self.get_offset()
            self.simutanious_update_spin_slide_combo(self.ui.spin_offset,
                                                     self.get_offset_auto_value())
        else:
            new_state = True
            value_before = self._spinbox_last_value[self.ui.spin_offset]
            self.ui.spin_offset.setValue(value_before)

        self.ui.spin_offset.setEnabled(new_state)
        self.ui.slide_offset.setEnabled(new_state)


    def check_auto_resize(self, state):
        if state == 2:
            manual_spinbox_enabled = False
            self.ui.hframe_preview.resizeEvent = self.update_label_and_preview_image_size_via_window_size
            self.update_label_and_preview_image_size_via_window_size()
        else:
            manual_spinbox_enabled = True
            self.ui.hframe_preview.resizeEvent = lambda unused: None
            self.update_label_and_preview_image_size_manually()

        for size_spinbox_item in self.collection_width_height_spinbox:
            size_spinbox_item.setEnabled(manual_spinbox_enabled)


    def src_num_changed(self):
        text = self.ui.source_numbers_text.toPlainText()
        # Remove non-numeric characters from the text
        cleaned_text = ''.join(filter(lambda x: x.isdigit(), text))
        if cleaned_text != text:
            cursor = self.ui.source_numbers_text.textCursor()
            cursor.movePosition(cursor.End)
            self.ui.source_numbers_text.setPlainText(cleaned_text)
            cursor.movePosition(cursor.End)
            self.ui.source_numbers_text.setTextCursor(cursor)

        self.reload_image()


    def get_source_text(self):
        return self.ui.source_numbers_text.toPlainText()


    def update_stero_module_parameters(self):
        """
        function updates the parameters of the stero_numbers module
        based on the current settings displayed on the UI (spinboxes)

        setting includes: FONT_SPACING, COL_SPACING, ROW_SPACING, OFFSET
        optional: size of the generated image

        the source numbers are not updated here; they are expected to be
        handled elsewhere.
        """

        # TODO: decide if width, hegiht of an image should be considered
        # update: update width and height with the functon below
        sn.FONT_SPACING = int(self.get_font_spacing())
        sn.COL_SPACING = int(self.get_col_spacing())
        sn.ROW_SPACING = int(max(self.get_row_spacing(), 1))
        sn.OFFSET = int(self.get_offset())

    def reload_image(self):
        self.update_stero_module_parameters()
        src_text = self.get_source_text()
        if src_text == "":
            src_text = sn.extract_source()
        sn.encode_numbers(src_text)
        self.ui.img_preview_label.setPixmap("preview.png")


    def update_label_and_review_image_size(self, width, height):
        self.ui.img_preview_label.resize(width, height)
        sn.redefine_image_and_draw(width, height)
        print(f"stero_mod and label size updated to {width}x{height}.")
        self.reload_image()


    def update_label_and_preview_image_size_manually(self):
        width = int(self.ui.width_adjust_spinbox.value())
        height = int(self.ui.height_adjust_spinbox.value())
        self.update_label_and_review_image_size(width, height)


    def update_label_and_preview_image_size_via_window_size(self, event=None):
        containing_frame_height = self.ui.vframe_preview.height()
        containing_frame_width = self.ui.vframe_preview.width()
        # min cutoff needed for width and height are 22 and 52 respectively to
        # prevent a window growing indefinitely because of feedback loop
        # 
        # however, over here we I *2 both cuttoff so that it's easier to size
        # down the window (bc windows cannot resize further than the size of
        # the label)
        self.update_label_and_review_image_size(containing_frame_width-22*2-10, 
                                           containing_frame_height-52*2)

    def update_gradient_settings(self, new_idx):
        sn.STERO_COLOR_GRADIENT = self.collection_gradients[new_idx]
        self.reload_image()

    # =================================== Dbg functions ===================================
    def read_value_out(self, value):
        print("Slider value:", value)

    def report_window_height(self):
        print(f"frame dim: {self.ui.vframe_preview.width()} {self.ui.vframe_preview.height()}")
        print(f"label dim: {self.ui.img_preview_label.width()} {self.ui.img_preview_label.height()}")

    def report_resize(self, event):
        event_size = event.size()
        # one method of getting new size
        print("Frame resized to:", event_size.width(), "x", event_size.height())

        # another method, does the same thing
        self.report_window_height()

    def import_via_builtin_file_select(self):
        file_dialog = QFileDialog()
        file_dialog.exec_()
        selected_files = file_dialog.selectedFiles()
        # print("Selected files:", selected_files) # it's a list
        fd = open(selected_files[0], "r")
        lines = fd.readlines()
        res = ""
        for line in lines: 
            res += line 
        # print(f"attempting to set: {res}")
        self.ui.source_numbers_text.setPlainText(res)

    def combo_box_report_idx(self, idx):
        print(idx)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
