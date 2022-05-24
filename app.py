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

    def ClickBoton(self):
        filtrito = LowPass.LowPass(float(self.omegaZero.text()))
        w, a, p = filtrito.getbode()
        self.Bode.plot(w, a, p)
        poles, zeros = filtrito.getpolesandzeros()
        self.PolesZeros.plot(poles, zeros)
        points = np.linspace(0, 1, 1000, endpoint=True)
        points4expr = np.linspace(0, 1, 500, endpoint=True)
        print(len(points), len(points4expr))
        points4expr = np.append(points4expr, points4expr)

        inputsignal = [1 for i in points]

        match self.inputComboBox.currentText():
            case 'Cos':
                inputsignal = float(self.InputAmpline.text()) * np.cos(points * 4 * np.pi)
            case 'Periodic Pulse':
                inputsignal = float(self.InputAmpline.text()) * signal.square(points * 4 * np.pi)
            case 'Pulse':
                print('Pulse')
                t = sp.Symbol('t', real=True)
                expr = parse_expr(self.InputAmpline.text(), local_dict={'t': t})
                print(expr)
                f = sp.lambdify(t, expr, "numpy")
                inputsignal = f(points4expr)
            case _:
                print('NADA')

        time, output = filtrito.getoutputfrominput(points*2/float(self.InputFreqLine.text()), inputsignal)
        self.InOut.plot(time, inputsignal, output)
