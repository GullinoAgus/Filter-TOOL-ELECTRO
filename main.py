import sys
from UI import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():

    app = QtWidgets.QApplication(sys.argv)
    Ventana = MainWindow()
    Ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
