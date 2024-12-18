import sys
import mainwindow

if __name__ == "__main__":
    window = mainwindow.QApplication(sys.argv)
    widget = mainwindow.MainWindow()
    widget.show()
    sys.exit(window.exec_())
