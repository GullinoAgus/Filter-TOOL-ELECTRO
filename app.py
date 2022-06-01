import io
import sys, logging
import tokenize

import numpy as np
import sympy as sp
from PyQt6 import QtWidgets, QtGui
from scipy import signal
from sympy.parsing.sympy_parser import parse_expr, T

import plotWidget as pw
from Filters import FirstOrder, SecondOrder
from UI import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        sp.init_printing()
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
        self.workingfilter

    def EnterTheMatrix(self):

        try:
            self.workingfilter = self.buildFilter()
            w, a, p = self.workingfilter.getbode()
            self.Bode.plot(w, a, p)
            poles, zeros = self.workingfilter.getpolesandzeros()
            self.PolesZeros.plot(poles, zeros)
            t, inputsignal = self.buildInput()

            time, output = self.workingfilter.getoutputfrominput(t, inputsignal)
            self.InOut.plot(time, inputsignal, output)
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")
            tupla = sys.exc_info()
            logging.error("Error:", tupla[0], "\n", tupla[1], "\n", tupla[2])
            pass
        except NameError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")
            tupla = sys.exc_info()
            logging.error("Error:", tupla[0], "\n", tupla[1], "\n", tupla[2])
            pass
        except AttributeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")
            tupla = sys.exc_info()
            logging.error("Error:", tupla[0], "\n", tupla[1], "\n", tupla[2])
            pass
        except TypeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: paso algo inesperado.")
            tupla = sys.exc_info()
            logging.error("Error:", tupla[0], "\n", tupla[1], "\n", tupla[2])
            pass
        except tokenize.TokenError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")
            tupla = sys.exc_info()
            logging.error("Error:", tupla[0], "\n", tupla[1], "\n", tupla[2])
            pass
        except SyntaxError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")
            tupla = sys.exc_info()
            logging.error("Error:", tupla[0], "\n", tupla[1], "\n", tupla[2])
            pass
        except:
            tupla = sys.exc_info()
            logging.critical("Error no capturado:", tupla[0], "\n", tupla[1], "\n", tupla[2])

    def buildFilter(self):  # TODO arreglar cuando la interfaz este completa
        if self.FORadio.isChecked():
            match self.FOComboBox.currentText():
                case 'Low Pass':
                    return FirstOrder.LowPass(self.CFSettingsDoubleSpinBox.value(),
                                              self.GainSettingsDoubleSpinBox.value())
                case 'High Pass':
                    return FirstOrder.HighPass(self.CFSettingsDoubleSpinBox.value(),
                                               self.GainSettingsDoubleSpinBox.value())
                case 'All Pass':
                    return FirstOrder.AllPass(self.CFSettingsDoubleSpinBox.value(),
                                              self.GainSettingsDoubleSpinBox.value())
                case 'Create new filter':
                    return FirstOrder.ArbitraryFO(self.PFAFSettingsDoubleSpinBox.value(),
                                                  self.ZFAFSettingsDoubleSpinBox.value(),
                                                  self.GainSettingsDoubleSpinBox.value())
                case _:
                    logging.debug('ERROR CASO DEFAULT DE buildFilter EN FIRST ORDER')
        elif self.SORadio.isChecked():
            match self.SOComboBox.currentText():  # TODO terminar matchcase de segundo orden
                case 'Low Pass':
                    if self.
                    return  SecondOrder.LowPass()
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
                    logging.debug('TODO')
                case _:
                    logging.debug('ERROR CASO DEFAULT DE buildFilter EN SECOND ORDER')

    def buildInput(self):  # TODO arreglar cuando la interfaz este completa
        points = np.linspace(0, 1, 1000, endpoint=True)
        points4expr = np.linspace(0, 1, 500, endpoint=True)
        points4expr = np.append(points4expr, points4expr)
        inputsignalpoints = None
        timepoints = points

        match self.ISComboBox.currentText():
            case 'Cos':
                inputsignalpoints = self.AInputSignalDoubleSpinBox2.value() * np.cos(points * 4 * np.pi)
                timepoints = points * 2 / self.FInputSignalDoubleSpinBox2.value()
            case 'Step':
                inputsignalpoints = [self.AInputSignalDoubleSpinBox1.value() for i in points]
            case 'Periodic Pulse':
                inputsignalpoints = self.AInputSignalDoubleSpinBox3.value() * \
                                    (signal.square(points * 4 * np.pi, self.DCInputSignalDoubleSpinBox3.value()) - 0.5)
                timepoints = points * 2 / self.FInputSignalDoubleSpinBox3.value()
            case 'Triangle Periodic Pulse':
                t = sp.Symbol('t', real=True)
                expr = self.AInputSignalDoubleSpinBox3.value() * sp.Piecewise((-t + 1 / 4, t <= 1 / 2),
                                                                              (t - 3 / 4, t > 1 / 2))
                f = sp.lambdify(t, expr, "numpy")
                inputsignalpoints = f(points4expr)
                timepoints = points * 2 / self.FInputSignalDoubleSpinBox3.value()
            case 'Other':
                t = sp.Symbol('t', real=True)
                expr = parse_expr(self.correctExpression(self.FuncInputSignalTextEdit4.text().replace('\n', '')),
                                  local_dict={'t': t}, transformations=T[:])
                
                try:
                    tex_expr_raw = io.BytesIO()
                    sp.preview(expr, output='png', viewer='BytesIO', outputbuffer=tex_expr_raw)
                    tex_expr_raw.seek(0)
                    tex_expr_qimage = QtGui.QImage.fromData(tex_expr_raw.read(), 'png')
                    tex_expr_pixmap = QtGui.QPixmap.fromImage(tex_expr_qimage)
                    self.labelforeq.setPixmap(tex_expr_pixmap)
                except:
                    self.labelforeq.setText('Error, you may not\n have latex installed')
                    
                f = sp.lambdify(t, expr, "numpy")
                inputsignalpoints = f(points4expr)
            case _:
                logging.error('CASO DEFAULT EN buildInput')

        return timepoints, inputsignalpoints

    def correctExpression(self, expr: str):
        validfuncs = sp.functions.__all__
        exprlower = expr.lower()
        correctedexpr = expr
        for funct in validfuncs:
            if funct.lower()+'(' in exprlower:
                correctedexpr = exprlower.replace(funct.lower(), funct)
        return correctedexpr


    def Prueba(self):
        logging.debug("Probando")

    def FORadioButtonActive(self, state):
        if state == True:
            self.FilterTypeStackedWidget.setCurrentIndex(0)

    def SORadioButtonActive(self, state):
        if state == True:
            self.FilterTypeStackedWidget.setCurrentIndex(1)

    def CurrFilterComboBox(self, index):
        logging.debug(index)

    def CurrInputComboBox(self, index):
        logging.debug(index)
