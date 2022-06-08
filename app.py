import sys
import tokenize
from main import logger
import numpy as np
import sympy as sp
from PyQt6 import QtWidgets
from scipy import signal
from sympy.parsing.sympy_parser import parse_expr, T
from RLC import RLC
import plotWidget as pw
from Filters import FirstOrder, SecondOrder
from UI import Ui_MainWindow

# FIXME Bug con ganancia maxima, se baja de mas en segundo orden

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
        self.workingfilter = None
        self.workingRLC = None

    def PlotBodeAndPoles(self):

        try:
            self.workingfilter = self.buildFilter()
            w, a, p = self.workingfilter.getbode()
            self.Bode.plot(w, a, p)
            poles, zeros = self.workingfilter.getpolesandzeros()
            self.PolesZeros.plot(poles, zeros)

        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")

            logger.error(sys.exc_info()[1])
            pass
        except NameError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")

            logger.error(sys.exc_info()[1])
            pass
        except AttributeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")

            logger.error(sys.exc_info()[1])
            pass
        except TypeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: paso algo inesperado.")

            logger.error(sys.exc_info()[1])
            pass
        except tokenize.TokenError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")

            logger.error(sys.exc_info()[1])
            pass
        except SyntaxError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")

            logger.error(sys.exc_info()[1])
            pass
        except ZeroDivisionError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: saca ese cero de ahi carajo.")
            pass
        except:

            logger.critical(sys.exc_info()[1])

    def EnterTheMatrix(self):

        try:
            self.PlotBodeAndPoles()
            t, inputsignal = self.buildInput()
            if self.ISComboBox.currentText() == 'δ Dirac':
                time, output = self.workingfilter.getoutputfrominput(impulse=True)
            else:
                time, output = self.workingfilter.getoutputfrominput(t, inputsignal)
            self.InOut.plot(time, inputsignal, output)

        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")

            logger.error(sys.exc_info()[1])
            pass
        except NameError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")

            logger.error(sys.exc_info()[1])
            pass
        except AttributeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")

            logger.error(sys.exc_info()[1])
            pass
        except TypeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: paso algo inesperado.")

            logger.error(sys.exc_info()[1])
            pass
        except tokenize.TokenError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")

            logger.error(sys.exc_info()[1])
            pass
        except SyntaxError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: La funcion ingresada tiene errores de sintaxis o no "
                                                          "contiene una funcion predefinida.")

            logger.error(sys.exc_info()[1])
            pass
        except ZeroDivisionError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: saca ese cero de ahi carajo.")
            pass
        except:

            logger.critical("Error no capturado:")
            logger.error(sys.exc_info()[1])

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
                    logger.debug('ERROR CASO DEFAULT DE buildFilter EN FIRST ORDER')
        elif self.SORadio.isChecked():
            match self.SOComboBox.currentText():  # TODO terminar matchcase de segundo orden
                case 'Low Pass':
                    xi = self.XiSettingsDoubleSpinBox3.value()
                    gain = self.GainSettingsDoubleSpinBox.value()
                    if 0 < xi < 1 / np.sqrt(2) and self.MGRadioButton.isChecked():
                        peak = 1 / (2 * xi * np.sqrt(1 - 2 * xi ** 2))
                        if peak > gain:
                            return SecondOrder.LowPass(self.RFSettingsDoubleSpinBox3.value(), xi, gain / peak)
                        else:
                            return SecondOrder.LowPass(self.RFSettingsDoubleSpinBox3.value(), xi)
                    elif self.BPGRadioButton.isChecked():
                        return SecondOrder.LowPass(self.RFSettingsDoubleSpinBox3.value(), xi, gain)
                    else:
                        return SecondOrder.LowPass(self.RFSettingsDoubleSpinBox3.value(), xi)

                case 'High Pass':
                    xi = self.XiSettingsDoubleSpinBox3.value()
                    gain = self.GainSettingsDoubleSpinBox.value()
                    if 0 < xi < 1 / np.sqrt(2) and self.MGRadioButton.isChecked():
                        peak = 1 / (2 * xi * np.sqrt(1 - 2 * xi ** 2))
                        if peak > gain:
                            return SecondOrder.HighPass(self.RFSettingsDoubleSpinBox3.value(), xi, gain / peak)
                        else:
                            return SecondOrder.HighPass(self.RFSettingsDoubleSpinBox3.value(), xi)
                    elif self.BPGRadioButton.isChecked():
                        return SecondOrder.HighPass(self.RFSettingsDoubleSpinBox3.value(), xi, gain)
                    else:
                        return SecondOrder.HighPass(self.RFSettingsDoubleSpinBox3.value(), xi)
                case 'All Pass':
                    return SecondOrder.AllPass(self.RFSettingsDoubleSpinBox3.value(),
                                               self.XiSettingsDoubleSpinBox3.value(),
                                               self.GainSettingsDoubleSpinBox.value())
                case 'Band Pass':
                    return SecondOrder.BandPass(self.RFSettingsDoubleSpinBox3.value(),
                                                self.XiSettingsDoubleSpinBox3.value(),
                                                self.GainSettingsDoubleSpinBox.value())
                case 'Notch':
                    return SecondOrder.NotchPass(self.RFSettingsDoubleSpinBox3.value(),
                                                 self.XiSettingsDoubleSpinBox3.value(),
                                                 self.GainSettingsDoubleSpinBox.value())
                case 'Create new filter':
                    if self.MGRadioButton.isChecked():
                        if self.NumeratorComboBox.currentIndex() == 0:
                            if self.WSettingsDoubleSpinBox41.value() == 0:
                                return SecondOrder.ArbitraryFilter(self.WSettingsDoubleSpinBox43.value(),
                                                                   self.XiSettingsDoubleSpinBox43.value(),
                                                                   [1, 0],
                                                                   maxGain=True)
                            else:
                                return SecondOrder.ArbitraryFilter(self.WSettingsDoubleSpinBox43.value(),
                                                                   self.XiSettingsDoubleSpinBox43.value(),
                                                                   [1 / self.WSettingsDoubleSpinBox41.value(), 1],
                                                                   k=self.GainSettingsDoubleSpinBox.value(),
                                                                   maxGain=True)
                        else:
                            return SecondOrder.ArbitraryFilter.secondordnum(self.WSettingsDoubleSpinBox43.value(),
                                                                            self.XiSettingsDoubleSpinBox43.value(),
                                                                            self.WSettingsDoubleSpinBox42.value(),
                                                                            self.XiSettingsDoubleSpinBox42.value(),
                                                                            k=self.GainSettingsDoubleSpinBox.value(),
                                                                            maxGain=True)
                    else:
                        if self.NumeratorComboBox.currentIndex() == 0:
                            if self.WSettingsDoubleSpinBox41.value() == 0:
                                return SecondOrder.ArbitraryFilter(self.WSettingsDoubleSpinBox43.value(),
                                                                   self.XiSettingsDoubleSpinBox43.value(),
                                                                   [1, 0],
                                                                   k=self.GainSettingsDoubleSpinBox.value())
                            else:
                                return SecondOrder.ArbitraryFilter(self.WSettingsDoubleSpinBox43.value(),
                                                                   self.XiSettingsDoubleSpinBox43.value(),
                                                                   [1 / self.WSettingsDoubleSpinBox41.value(), 1],
                                                                   k=self.GainSettingsDoubleSpinBox.value())
                        else:
                            return SecondOrder.ArbitraryFilter.secondordnum(self.WSettingsDoubleSpinBox43.value(),
                                                                            self.XiSettingsDoubleSpinBox43.value(),
                                                                            self.WSettingsDoubleSpinBox42.value(),
                                                                            self.XiSettingsDoubleSpinBox42.value(),
                                                                            k=self.GainSettingsDoubleSpinBox.value())
                case _:
                    logger.debug('ERROR CASO DEFAULT DE buildFilter EN SECOND ORDER')

    def buildInput(self):  # TODO arreglar cuando la interfaz este completa
        points = np.linspace(0, 1, 1000, endpoint=True)
        points4expr = np.linspace(0, 1, 500, endpoint=True)
        points4expr = np.append(points4expr, points4expr)
        inputsignalpoints = None
        timepoints = points

        match self.ISComboBox.currentText():
            case 'Cos':
                inputsignalpoints = self.AInputSignalDoubleSpinBox2.value() * np.cos(points * 4 * np.pi)
                timepoints = points * 4 * np.pi / self.FInputSignalDoubleSpinBox2.value()
            case 'Step':
                inputsignalpoints = [self.AInputSignalDoubleSpinBox1.value() for i in points]
            case 'Periodic Pulse':
                inputsignalpoints = self.AInputSignalDoubleSpinBox3.value() * \
                                    (signal.square(points * 4 * np.pi, self.DCInputSignalDoubleSpinBox3.value()))
                timepoints = points * 4 * np.pi / self.FInputSignalDoubleSpinBox3.value()
            case 'Triangle Periodic Pulse':
                t = sp.Symbol('t', real=True)
                DC = self.DCInputSignalDoubleSpinBox3.value()
                if DC == 0:
                    expr = self.AInputSignalDoubleSpinBox3.value() * (-2 * t + 1)
                elif DC == 1:
                    expr = self.AInputSignalDoubleSpinBox3.value() * (2 * t - 1)
                else:
                    expr = self.AInputSignalDoubleSpinBox3.value() * \
                           sp.Piecewise((2 / DC * t - 1, t <= DC), (-2 / (1 - DC) * t + 2 / (1 - DC) - 1, t > DC))
                f = sp.lambdify(t, expr, "numpy")
                inputsignalpoints = f(points4expr)
                timepoints = points * 4 * np.pi / self.FInputSignalDoubleSpinBox3.value()
            case 'δ Dirac':
                timepoints = [0]
                inputsignalpoints = [1]
            case 'Other':
                t = sp.Symbol('t', real=True)
                expr = parse_expr(self.correctExpression(self.FuncInputSignalTextEdit4.toPlainText().replace('\n', '')),
                                  local_dict={'t': t}, transformations=T[:])
                f = sp.lambdify(t, expr, "numpy")
                inputsignalpoints = f(points4expr)
                timepoints = points * 4 * np.pi / self.FInputSignalDoubleSpinBox4.value()
            case _:
                logger.error('CASO DEFAULT EN buildInput')

        return timepoints, inputsignalpoints

    def correctExpression(self, expr: str):
        validfuncs = sp.functions.__all__
        exprlower = expr.lower()
        correctedexpr = expr
        for funct in validfuncs:
            if funct.lower() + '(' in exprlower:
                correctedexpr = exprlower.replace(funct.lower(), funct)
        return correctedexpr

    def FORadioButtonActive(self, state):
        if state:
            self.FilterTypeStackedWidget.setCurrentIndex(0)
            self.CurrFOFilterComboBox(self.FOComboBox.currentIndex())

    def SORadioButtonActive(self, state):
        if state:
            self.FilterTypeStackedWidget.setCurrentIndex(1)
            self.CurrSOFilterComboBox(self.SOComboBox.currentIndex())

    def CurrFOFilterComboBox(self, index):  # Combo box de los filtros de primer orden
        if index == 3:
            self.FilterInfoStackedWidget.setCurrentIndex(1)
        else:
            self.FilterInfoStackedWidget.setCurrentIndex(0)

    def CurrSOFilterComboBox(self, index):  # Combo box de los filtros de segundo orden
        if index == 5:
            self.FilterInfoStackedWidget.setCurrentIndex(3)
        else:
            self.FilterInfoStackedWidget.setCurrentIndex(2)

    def CurrInputSignalComboBox(self, index):
        if index == 1:
            self.InputTypeStackedWidget.setCurrentIndex(0)
        elif index == 2 or index == 3:
            self.InputTypeStackedWidget.setCurrentIndex(2)
        elif index == 5:
            self.InputTypeStackedWidget.setCurrentIndex(3)
        elif index == 4:
            self.InputTypeStackedWidget.setCurrentIndex(4)
        else:
            self.InputTypeStackedWidget.setCurrentIndex(1)

    '''
    Slots for RLC section
    '''
    
    def calculateRLC(self):
        return
    
    def calculateRLCInput(self):
        return
    
    def buildRLC(self):
        try:
            self.workingRLC
        
        except ValueError:
            pass
            