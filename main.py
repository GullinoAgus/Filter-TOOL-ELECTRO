# noinspection PyUnresolvedReferences
import sys
from Filters import LowPass
import numpy as np
from UI import *


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
    #prueba = LowPass.LowPass(50000)
    #prueba.plotgain()
    #time = np.linspace(0, 4 * np.pi, 500)
    #prueba.plotoutput(time, np.cos(time))
    aplicacion = QtWidgets.QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(aplicacion.exec())


if __name__ == "__main__":
    main()
