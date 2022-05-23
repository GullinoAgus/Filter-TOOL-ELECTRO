# noinspection PyUnresolvedReferences
import sys
from Filters import LowPass
import numpy as np
from UI import *
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    @staticmethod
    def ClickBoton():
        print("Matame")

    def Prueba(self):
        print("Probando");

    def FORadioButtonActive(self, state):
        if state == True:
            self.FilterTypeStackedWidget.setCurrentIndex(0);

    def SORadioButtonActive(self, state):
        if state == True:
            self.FilterTypeStackedWidget.setCurrentIndex(1);

    def CurrFilterComboBox(self, index):
        print(index);

    def CurrInputComboBox(self, index):
        print(index);

def main():
    aplicacion = QtWidgets.QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(aplicacion.exec())


if __name__ == "__main__":
    main()
