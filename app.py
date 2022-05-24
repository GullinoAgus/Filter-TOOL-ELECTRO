import numpy as np
from scipy import signal
from Filters import LowPass
import plotWidget as pw
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from UI import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Bode = pw.BodePlot(parent=self.BodePlotBox)
        self.InOut = pw.InOutPlot(parent=self.InputAndOutputBox)
        self.PolesZeros = pw.PolesZerosPlot(parent=self.PolesAndZerosBox)
        self.BodePlotBox.layout().addWidget(self.Bode.navToolBar)
        self.BodePlotBox.layout().addWidget(self.Bode)
        self.PolesAndZerosBox.layout().addWidget(self.PolesZeros.navToolBar)
        self.PolesAndZerosBox.layout().addWidget(self.PolesZeros)
        self.InputAndOutputBox.layout().addWidget(self.InOut.navToolBar)
        self.InputAndOutputBox.layout().addWidget(self.InOut)

    def EnterTheMatrix(self):
        filtrito = LowPass.LowPass(float(self.PFSettingsLineEdit.text()))
        w, a, p = filtrito.getbode()
        self.Bode.plot(w, a, p)
        poles, zeros = filtrito.getpolesandzeros()
        self.PolesZeros.plot(poles, zeros)
        points = np.linspace(0, 1, 1000, endpoint=True)
        points4expr = np.linspace(0, 1, 500, endpoint=True)
        print(len(points), len(points4expr))
        points4expr = np.append(points4expr, points4expr)

        inputsignalpoints = [1 for i in points]

        match self.ISComboBox.currentText():
            case 'Cos':
                inputsignalpoints = float(self.AInputSignalLineEdit.text()) * np.cos(points * 4 * np.pi)
            case 'Periodic Pulse':
                inputsignalpoints = float(self.AInputSignalLineEdit.text()) * signal.square(points * 4 * np.pi)
            case 'Other':
                t = sp.Symbol('t', real=True)
                expr = parse_expr(self.AInputSignalLineEdit.text(), local_dict={'t': t})
                print(expr)
                f = sp.lambdify(t, expr, "numpy")
                inputsignalpoints = f(points4expr)
            case _:
                print('NADA')

        time, output = filtrito.getoutputfrominput(points*2/float(self.FInputSignalLineEdit.text()), inputsignalpoints)
        self.InOut.plot(time, inputsignalpoints, output)

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