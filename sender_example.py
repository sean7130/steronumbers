import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget, QSpinBox, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multiple Sliders Example")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.sliders = []
        self.last_changed_slider = None  # Variable to store the last changed slider

        for i in range(3):  # Create three sliders
            slider = QSlider()
            slider.setOrientation(1)  # Vertical orientation
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.valueChanged.connect(self.slider_value_changed)
            self.sliders.append(slider)
            layout.addWidget(slider)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def slider_value_changed(self, value):
        sender = self.sender()  # Get the sender of the signal
        self.last_changed_slider = sender  # Update the last changed slider
        print("Slider value changed to:", value, "by", sender)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
