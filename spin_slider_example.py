import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget, QSpinBox, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Slider and SpinBox Example (values affect each other)")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(1)  # Vertical orientation
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(0)
        self.spin_box.setMaximum(10000)

        self.slider.valueChanged.connect(self.slider_value_changed)
        self.spin_box.valueChanged.connect(self.spin_box_value_changed)

        layout.addWidget(self.slider)
        layout.addWidget(self.spin_box)

        self.btn_change_value = QPushButton("Change SpinBox Value")
        self.btn_change_value.clicked.connect(self.change_spin_box_value)
        layout.addWidget(self.btn_change_value)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.lock = False

    def slider_value_changed(self, value):
        if not self.lock:
            print(f"slider_value_changed: {value}")
            self.lock = True
            self.spin_box.setValue(value * 100)
            self.lock = False

    def spin_box_value_changed(self, value):
        if not self.lock:
            print(f"spin_box_value_changed: {value}")
            self.lock = True
            self.slider.setValue(value)
            self.lock = False

    def change_spin_box_value(self):
        new_value = 75
        self.spin_box.setValue(new_value)
        print("SpinBox value changed to:", new_value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
