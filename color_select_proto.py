import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QColorDialog
from PyQt5.QtGui import QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color Selector Example")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.button = QPushButton("Select Color")
        self.button.clicked.connect(self.open_color_dialog)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_color_dialog(self):
        color_dialog = QColorDialog(self)
        color = color_dialog.getColor()
        if color.isValid():
            print("Selected color:", color.getRgb())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
