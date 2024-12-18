import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout

class Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog Example")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        layout.addWidget(QPushButton("OK"))
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window Example")
        self.setGeometry(100, 100, 400, 300)

        button = QPushButton("Open Dialog")
        button.clicked.connect(self.open_dialog)
        self.setCentralWidget(button)

    def open_dialog(self):
        dialog = Dialog()
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
