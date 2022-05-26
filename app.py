import io
import sys
import tokenize

import numpy as np
import sympy as sp
from PyQt6 import QtWidgets, QtGui
from scipy import signal
from sympy.parsing.sympy_parser import parse_expr

import plotWidget as pw
from Filters import FirstOrder
from UI import Ui_MainWindow


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
        self.labelforeq = QtWidgets.QLabel()
        self.gridLayout_6.addWidget(self.labelforeq, 2,1)

    def EnterTheMatrix(self):

        try:
            filtro = self.buildFilter()
            w, a, p = filtro.getbode()
            self.Bode.plot(w, a, p)
            poles, zeros = filtro.getpolesandzeros()
            self.PolesZeros.plot(poles, zeros)
            t, inputsignal = self.buildInput()

            time, output = filtro.getoutputfrominput(t, inputsignal)
            self.InOut.plot(time, inputsignal, output)
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")
            tupla = sys.exc_info()
            print(tupla[1])
            pass
        except NameError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")
            pass
        except AttributeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")
            pass
        except TypeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: paso algo inesperado.")
            tupla = sys.exc_info()
            print(tupla)
            pass
        except tokenize.TokenError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")
            pass
        except SyntaxError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")
            pass
        except:
            tupla = sys.exc_info()
            print(tupla[1])

    def buildFilter(self):  # TODO arreglar cuando la interfaz este completa
        if self.FORadio.isChecked():
            match self.FOComboBox.currentText():
                case 'Low Pass':
                    return FirstOrder.LowPass(float(self.PFSettingsLineEdit.text()))
                case 'High Pass':
                    return FirstOrder.HighPass(float(self.PFSettingsLineEdit.text()))
                case 'All Pass':
                    return FirstOrder.AllPass(float(self.PFSettingsLineEdit.text()))
                case 'Create new filter':  # TODO terminar Create new filter de primer orden
                    print('TODO')
                case _:
                    print('No es por ahi')
        elif self.SORadio.isChecked():
            match self.SOComboBox.currentText():  # TODO terminar matchcase de segundo orden
                case 'Low Pass':
                    return FirstOrder.LowPass(float(self.PFSettingsLineEdit.text()))
                case 'High Pass':
                    return FirstOrder.HighPass(float(self.PFSettingsLineEdit.text()))
                case 'All Pass':
                    return FirstOrder.AllPass(float(self.PFSettingsLineEdit.text()))
                case 'Band Pass':
                    return FirstOrder.AllPass(float(self.PFSettingsLineEdit.text()))
                case 'Notch':
                    return FirstOrder.AllPass(float(self.PFSettingsLineEdit.text()))
                case 'Low-Pass Notch':
                    return FirstOrder.AllPass(float(self.PFSettingsLineEdit.text()))
                case 'High-Pass Notch':
                    return FirstOrder.AllPass(float(self.PFSettingsLineEdit.text()))
                case 'Create new filter':
                    print('TODO')
                case _:
                    print('No es por ahi')

    def buildInput(self):  # TODO arreglar cuando la interfaz este completa
        points = np.linspace(0, 1, 1000, endpoint=True)
        points4expr = np.linspace(0, 1, 500, endpoint=True)
        points4expr = np.append(points4expr, points4expr)
        inputsignalpoints = None

        match self.ISComboBox.currentText():
            case 'Cos':
                inputsignalpoints = float(self.AInputSignalLineEdit.text()) * np.cos(points * 4 * np.pi)
            case 'Step':
                inputsignalpoints = [1 for i in points]
            case 'Periodic Pulse':
                inputsignalpoints = float(self.AInputSignalLineEdit.text()) * (signal.square(points * 4 * np.pi) - 0.5)
            case 'Triangle Periodic Pulse':
                t = sp.Symbol('t', real=True)
                expr = float(self.AInputSignalLineEdit.text()) * sp.Piecewise((-t + 1 / 4, t <= 1 / 2),
                                                                              (t - 3 / 4, t > 1 / 2))
                f = sp.lambdify(t, expr, "numpy")
                inputsignalpoints = f(points4expr)
            case 'Other':
                t = sp.Symbol('t', real=True)
                expr = parse_expr(self.correctExpression(self.AInputSignalLineEdit.text()), local_dict={'t': t})
                bytsitos = io.BytesIO()
                sp.preview(expr, output='png', viewer='BytesIO', outputbuffer=bytsitos)
                bytsitos.seek(0)
                qimagen = QtGui.QImage.fromData(bytsitos.read(), 'png')
                pixmapa = QtGui.QPixmap.fromImage(qimagen)
                self.labelforeq.setPixmap(pixmapa)
                f = sp.lambdify(t, expr, "numpy")
                inputsignalpoints = f(points4expr)
            case _:
                print('NADA')

        return points * 2 / float(self.FInputSignalLineEdit.text()), inputsignalpoints

    def correctExpression(self, expr: str):
        validfuncs = sp.functions.__all__
        exprlower = expr.lower()
        correctedexpr = expr
        for funct in validfuncs:
            if funct.lower()+'(' in exprlower:
                correctedexpr = exprlower.replace(funct.lower(), funct)
        return correctedexpr


    def Prueba(self):
        print("Probando")

    def FORadioButtonActive(self, state):
        if state == True:
            self.FilterTypeStackedWidget.setCurrentIndex(0)

    def SORadioButtonActive(self, state):
        if state == True:
            self.FilterTypeStackedWidget.setCurrentIndex(1)

    def CurrFilterComboBox(self, index):
        print(index)

    def CurrInputComboBox(self, index):
        print(index)
