import sys
import tokenize
from main import my_logger
import numpy as np
import sympy as sp
from PyQt6 import QtWidgets, QtGui
from scipy import signal
from sympy.parsing.sympy_parser import parse_expr, T
from RLC.RLC import RLC
import plotWidget as pw
from Filters import FirstOrder, SecondOrder
from UI import Ui_MainWindow
import os


# Funcion utilizada para obtener el path completo. Util para cuando se compacta todò en un binario.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Fucnion para corregir expresiones de las entradas de funciones en texto
def correctExpression(expr: str):
    validfuncs = sp.functions.__all__
    exprlower = expr.lower()
    correctedexpr = expr
    for funct in validfuncs:
        if funct.lower() + '(' in exprlower:
            correctedexpr = exprlower.replace(funct.lower(), funct)
    return correctedexpr


# Clase principal.
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Inicializacion de la GUI
        self.setupUi(self)
        icono = QtGui.QIcon(resource_path('icon.png'))
        self.setWindowIcon(icono)
        # Creacion y posicionamiento de los widgets de ploteo
        self.Bode = pw.BodePlot(parent=self.BodePlotBox)
        self.InOut = pw.InOutPlot(parent=self.InputAndOutputBox)
        self.PolesZeros = pw.PolesZerosPlot(parent=self.PolesAndZerosBox)
        self.RLCBode = pw.BodePlot(parent=self.RLCBodePlotBox)
        self.RLCInOut = pw.InOutPlot(parent=self.RLCInputPlotBox)
        self.BodePlotBox.layout().addWidget(self.Bode.navToolBar)
        self.BodePlotBox.layout().addWidget(self.Bode)
        self.PolesAndZerosBox.layout().addWidget(self.PolesZeros.navToolBar)
        self.PolesAndZerosBox.layout().addWidget(self.PolesZeros)
        self.InputAndOutputBox.layout().addWidget(self.InOut.navToolBar)
        self.InputAndOutputBox.layout().addWidget(self.InOut)
        self.RLCBodePlotBox.layout().addWidget(self.RLCBode.navToolBar)
        self.RLCBodePlotBox.layout().addWidget(self.RLCBode)
        self.RLCInputPlotBox.layout().addWidget(self.RLCInOut.navToolBar)
        self.RLCInputPlotBox.layout().addWidget(self.RLCInOut)
        # Se coloca la imagen del circuito en la GUI. Se puede hacer desde el QTDesigner pero no lo podria compilar
        # en un binario porque hay que usar resource_path()
        ImageRLC = QtGui.QPixmap(resource_path('RLC.png'))
        self.RLCImage.setPixmap(ImageRLC)
        # Datos miembro para contener a los filtros que se construyen
        self.workingfilter = None
        self.workingRLC = None

    # Callback para completar los ploteos de Bode y Polos y ceros de la Filter Tool
    def PlotBodeAndPoles(self):

        try:
            # Se construye el filtro de acuerdo a los valores ingresados
            self.workingfilter = self.buildFilter()
            # Se completan los ploteos de Bode y polos y ceros
            w, a, p = self.workingfilter.getbode()
            self.Bode.plot(w, a, p)
            poles, zeros = self.workingfilter.getpolesandzeros()
            self.PolesZeros.plot(poles, zeros)

        # Control de Excepciones
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")

            my_logger.error(sys.exc_info()[1])
            pass
        except TypeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: paso algo inesperado.")

            my_logger.error(sys.exc_info()[1])
            pass
        except ZeroDivisionError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: saca ese cero de ahi carajo.")

            my_logger.error(sys.exc_info()[1])
            pass
        except:

            my_logger.critical(sys.exc_info()[1])

    # Callback para la simulacion de salida en base a una funcion de entrada de la Filter Tool
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

            my_logger.error(sys.exc_info()[1])
            pass
        except NameError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")

            my_logger.error(sys.exc_info()[1])
            pass
        except AttributeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")

            my_logger.error(sys.exc_info()[1])
            pass
        except TypeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: paso algo inesperado.")

            my_logger.error(sys.exc_info()[1])
            pass
        except tokenize.TokenError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")

            my_logger.error(sys.exc_info()[1])
            pass
        except SyntaxError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")

            my_logger.error(sys.exc_info()[1])
            pass
        except ZeroDivisionError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: saca ese cero de ahi carajo.")
            pass
        except:
            my_logger.critical(sys.exc_info()[1])

    # Metodo fabricador de filtros
    def buildFilter(self):
        if self.FORadio.isChecked():
            match self.FOComboBox.currentText():
                # Todos los casos verifican si se seleccion ganancia maxima o de banda pasante
                case 'Low Pass':
                    if self.MGRadioButton.isChecked():
                        return FirstOrder.LowPass(self.CFSettingsDoubleSpinBox.value())
                    return FirstOrder.LowPass(self.CFSettingsDoubleSpinBox.value(),
                                              self.GainSettingsDoubleSpinBox.value())
                case 'High Pass':
                    if self.MGRadioButton.isChecked():
                        return FirstOrder.HighPass(self.CFSettingsDoubleSpinBox.value())
                    return FirstOrder.HighPass(self.CFSettingsDoubleSpinBox.value(),
                                               self.GainSettingsDoubleSpinBox.value())
                case 'All Pass':
                    if self.MGRadioButton.isChecked():
                        return FirstOrder.AllPass(self.CFSettingsDoubleSpinBox.value())
                    return FirstOrder.AllPass(self.CFSettingsDoubleSpinBox.value(),
                                              self.GainSettingsDoubleSpinBox.value())
                case 'Create new filter':
                    if self.MGRadioButton.isChecked():
                        return FirstOrder.ArbitraryFO(self.PFAFSettingsDoubleSpinBox.value(),
                                                      self.ZFAFSettingsDoubleSpinBox.value())
                    return FirstOrder.ArbitraryFO(self.PFAFSettingsDoubleSpinBox.value(),
                                                  self.ZFAFSettingsDoubleSpinBox.value(),
                                                  self.GainSettingsDoubleSpinBox.value())
                case _:
                    my_logger.critical('ERROR CASO DEFAULT DE buildFilter EN FIRST ORDER')

        elif self.SORadio.isChecked():
            match self.SOComboBox.currentText():
                case 'Low Pass':
                    xi = self.XiSettingsDoubleSpinBox3.value()
                    gain = self.GainSettingsDoubleSpinBox.value()
                    # Ajustes por seleccion de ganacia de banda pasante o ganancia maxima
                    if 0 < xi < 1 / np.sqrt(2) and self.MGRadioButton.isChecked():
                        peak = 1 / (2 * xi * np.sqrt(1 - 2 * xi ** 2))
                        if peak > np.abs(gain):
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
                    # Ajustes por seleccion de ganacia de banda pasante o ganancia maxima
                    if 0 < xi < 1 / np.sqrt(2) and self.MGRadioButton.isChecked():  # Seleccion: Ganancia Maxima
                        peak = 1 / (2 * xi * np.sqrt(1 - 2 * xi ** 2))
                        if peak > np.abs(gain):
                            return SecondOrder.HighPass(self.RFSettingsDoubleSpinBox3.value(), xi, gain / peak)
                        else:
                            return SecondOrder.HighPass(self.RFSettingsDoubleSpinBox3.value(), xi)
                    elif self.BPGRadioButton.isChecked():  # Seleccion: Ganancia de Banda Pasante
                        return SecondOrder.HighPass(self.RFSettingsDoubleSpinBox3.value(), xi, gain)
                    else:
                        return SecondOrder.HighPass(self.RFSettingsDoubleSpinBox3.value(), xi)
                case 'All Pass':
                    if self.MGRadioButton.isChecked():  # Seleccion: Ganancia Maxima
                        return SecondOrder.AllPass(self.RFSettingsDoubleSpinBox3.value(),
                                                   self.XiSettingsDoubleSpinBox3.value())
                    else:
                        return SecondOrder.AllPass(self.RFSettingsDoubleSpinBox3.value(),
                                                   self.XiSettingsDoubleSpinBox3.value(),
                                                   self.GainSettingsDoubleSpinBox.value())
                case 'Band Pass':
                    if self.MGRadioButton.isChecked():  # Seleccion: Ganancia Maxima
                        if np.abs(self.GainSettingsDoubleSpinBox.value()) < 1:
                            return SecondOrder.BandPass(self.RFSettingsDoubleSpinBox3.value(),
                                                        self.XiSettingsDoubleSpinBox3.value(),
                                                        self.GainSettingsDoubleSpinBox.value())
                        else:
                            return SecondOrder.BandPass(self.RFSettingsDoubleSpinBox3.value(),
                                                        self.XiSettingsDoubleSpinBox3.value())
                    else:   # Seleccion: Ganancia de Banda Pasante
                        return SecondOrder.BandPass(self.RFSettingsDoubleSpinBox3.value(),
                                                    self.XiSettingsDoubleSpinBox3.value(),
                                                    self.GainSettingsDoubleSpinBox.value())
                case 'Notch':
                    if self.MGRadioButton.isChecked():  # Seleccion: Ganancia Maxima
                        if np.abs(self.GainSettingsDoubleSpinBox.value()) < 1:
                            return SecondOrder.NotchPass(self.RFSettingsDoubleSpinBox3.value(),
                                                         self.XiSettingsDoubleSpinBox3.value(),
                                                         self.GainSettingsDoubleSpinBox.value())
                        else:
                            return SecondOrder.NotchPass(self.RFSettingsDoubleSpinBox3.value(),
                                                         self.XiSettingsDoubleSpinBox3.value())
                    else:   # Seleccion: Ganancia de Banda Pasante
                        return SecondOrder.NotchPass(self.RFSettingsDoubleSpinBox3.value(),
                                                     self.XiSettingsDoubleSpinBox3.value(),
                                                     self.GainSettingsDoubleSpinBox.value())
                case 'Create new filter':
                    if self.MGRadioButton.isChecked():  # Seleccion: Ganancia Maxima
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
                    else:   # Seleccion: Ganancia de Banda Pasante
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
                    my_logger.critical('ERROR CASO DEFAULT DE buildFilter EN SECOND ORDER')

    # Metodo para preparar el arreglo con los valores de amplitud y tiempo para excitar el sistema(Filtros)
    # Todas las señales se calculan de 0 a 1 y luego se ajusta el tiempo para que corresponda con la frecuencia
    # seleccionada
    def buildInput(self):
        periods_quant = self.TQUANTDoubleSpinBox.value()    # Cantidad de periodos a calcular
        points = np.linspace(0, periods_quant, int(1000 * periods_quant), endpoint=True)
        inputsignalpoints = None
        timepoints = points

        match self.ISComboBox.currentText():
            case 'Cos':
                inputsignalpoints = self.AInputSignalDoubleSpinBox2.value() * np.cos(points * 2 * np.pi)
                timepoints = points * 2 * np.pi / self.FInputSignalDoubleSpinBox2.value()
            case 'Step':
                inputsignalpoints = [self.AInputSignalDoubleSpinBox1.value() for i in points]
            case 'Periodic Pulse':
                inputsignalpoints = self.AInputSignalDoubleSpinBox3.value() * \
                                    (signal.square(points * 2 * np.pi, self.DCInputSignalDoubleSpinBox3.value()))

                timepoints = points * 2 * np.pi / self.FInputSignalDoubleSpinBox3.value()
            case 'Triangle Periodic Pulse':
                t = sp.Symbol('t', real=True)
                DC = self.DCInputSignalDoubleSpinBox3.value()   # Duty Cycle
                if DC == 0:
                    expr = self.AInputSignalDoubleSpinBox3.value() * (-2 * t + 1)
                elif DC == 1:
                    expr = self.AInputSignalDoubleSpinBox3.value() * (2 * t - 1)
                else:
                    expr = self.AInputSignalDoubleSpinBox3.value() * \
                           sp.Piecewise((2 / DC * t - 1, t <= DC), (-2 / (1 - DC) * t + 2 / (1 - DC) - 1, t > DC))
                f = sp.lambdify(t, expr, "numpy")

                inputsignalpoints = f(np.linspace(0, 1, 1000))
                if periods_quant.is_integer():
                    inputsignalpoints = np.tile(inputsignalpoints, int(periods_quant))
                else:
                    inputsignalpoints = np.tile(inputsignalpoints, int(np.floor(periods_quant) + 1))
                    indexlimit = int(1000 * periods_quant)
                    inputsignalpoints = inputsignalpoints[0:indexlimit]
                timepoints = points * 2 * np.pi / self.FInputSignalDoubleSpinBox3.value()
            case 'δ Dirac':
                timepoints = [0]
                inputsignalpoints = [1]
            case 'Other':
                t = sp.Symbol('t', real=True)   # Variable de expresion

                # Se Toma la expresion ingresada por el usuario, se corrije y se interpreta
                expr = parse_expr(
                    correctExpression(self.FuncInputSignalTextEdit4.toPlainText().replace('\n', '')),
                    local_dict={'t': t}, transformations=T[:])

                # Transformamos la expresion en un funcion Lambda para poder utilizarla
                f = sp.lambdify(t, expr, "numpy")

                # genero los puntos para la señal de entrada
                inputsignalpoints = f(np.linspace(0, 1, 1000))

                if periods_quant.is_integer():  # Cantidad entera de periodos
                    inputsignalpoints = np.tile(inputsignalpoints, int(periods_quant))
                else:   # Cantidad real de periodos
                    inputsignalpoints = np.tile(inputsignalpoints, int(np.floor(periods_quant) + 1))
                    indexlimit = int(1000 * periods_quant)
                    inputsignalpoints = inputsignalpoints[0:indexlimit]
                # Ajusto los puntos de X a la frecuecnia ingresada
                timepoints = points * 2 * np.pi / self.FInputSignalDoubleSpinBox4.value()
            case _:
                my_logger.error('CASO DEFAULT EN buildInput')

        return timepoints, inputsignalpoints

    # Callback para Ajustar los tipos de filtros a primer orden
    def FORadioButtonActive(self, state):
        if state:
            self.FilterTypeStackedWidget.setCurrentIndex(0)
            self.CurrFOFilterComboBox(self.FOComboBox.currentIndex())

    # Callback para ajustar los tipos de filtros a segundo orden
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

    def CurrInputSignalComboBox(self, index):   # Combo box para los tipos de señales de entrada
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

    # Prepara el RLC y plotea Bode y polos y ceros
    def calculateRLC(self):
        if self.MeasurPointComboBox.currentIndex() == -1 or self.ReferenceComboBox.currentIndex() == -1:
            return

        try:

            self.workingRLC = RLC(self.RvalueDoubleSpinBox.value(),
                                  self.LvalueDoubleSpinBox.value(),
                                  self.CvalueDoubleSpinBox.value() * 1e-6,
                                  int(self.MeasurPointComboBox.currentText()),
                                  int(self.ReferenceComboBox.currentText()))
            self.w0Label.setText("{:.3E}".format(self.workingRLC.get_resonant_freq()))
            self.QLabel.setText("{:.2f}".format(self.workingRLC.get_Q()))
            w, a, p = self.workingRLC.get_bode()
            self.RLCBode.plot(w, a, p)
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error: {sys.exc_info()[1]}.")

            my_logger.error(sys.exc_info()[1])
            pass
        except TypeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: paso algo inesperado.")

            my_logger.error(sys.exc_info()[1])
            pass
        except ZeroDivisionError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: saca ese cero de ahi carajo.")
            pass
        except:

            my_logger.critical(sys.exc_info()[1])

    # Callback para la simulacion de salida en base a una funcion de entrada de la RLC Tool
    def calculateRLCInput(self):
        try:
            self.calculateRLC()
            t, inputsignal = self.buildRLCInput()
            if self.ISComboBox_2.currentText() == 'δ Dirac':
                time, output = self.workingRLC.get_output_from_input(impulse=True)
            else:
                time, output = self.workingRLC.get_output_from_input(t, inputsignal)
            self.RLCInOut.plot(time, inputsignal, output)

        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")

            my_logger.error(sys.exc_info()[1])
            pass
        except NameError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")

            my_logger.error(sys.exc_info()[1])
            pass
        except AttributeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")

            my_logger.error(sys.exc_info()[1])
            pass
        except TypeError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: paso algo inesperado.")

            my_logger.error(sys.exc_info()[1])
            pass
        except tokenize.TokenError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")

            my_logger.error(sys.exc_info()[1])
            pass
        except SyntaxError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: Valores invalidos.")

            my_logger.error(sys.exc_info()[1])
            pass
        except ZeroDivisionError:
            QtWidgets.QMessageBox.critical(self, "Error", "Error: saca ese cero de ahi carajo.")
            pass
        except:

            my_logger.critical("Error no capturado:")
            my_logger.error(sys.exc_info()[1])

    def buildRLCInput(self):
        periods_quant = self.TQUANTDoubleSpinBox_2.value()  # Cantidad de periodos a calcular
        points = np.linspace(0, periods_quant, int(1000 * periods_quant), endpoint=True)
        inputsignalpoints = None
        timepoints = points

        match self.ISComboBox_2.currentText():
            case 'Cos':
                inputsignalpoints = self.AInputSignalDoubleSpinBox2_2.value() * np.cos(points * 2 * np.pi)
                timepoints = points * 2 * np.pi / self.FInputSignalDoubleSpinBox2_2.value()
            case 'Step':
                inputsignalpoints = [self.AInputSignalDoubleSpinBox1_2.value() for i in points]
            case 'Periodic Pulse':
                inputsignalpoints = self.AInputSignalDoubleSpinBox3_2.value() * \
                                    (signal.square(points * 2 * np.pi, self.DCInputSignalDoubleSpinBox3_2.value()))
                timepoints = points * 2 * np.pi / self.FInputSignalDoubleSpinBox3_2.value()
            case 'Triangle Periodic Pulse':
                t = sp.Symbol('t', real=True)
                DC = self.DCInputSignalDoubleSpinBox3_2.value() # Duty Cycle
                if DC == 0:
                    expr = self.AInputSignalDoubleSpinBox3_2.value() * (-2 * t + 1)
                elif DC == 1:
                    expr = self.AInputSignalDoubleSpinBox3_2.value() * (2 * t - 1)
                else:
                    expr = self.AInputSignalDoubleSpinBox3_2.value() * \
                           sp.Piecewise((2 / DC * t - 1, t <= DC), (-2 / (1 - DC) * t + 2 / (1 - DC) - 1, t > DC))
                f = sp.lambdify(t, expr, "numpy")
                inputsignalpoints = f(np.linspace(0, 1, 1000))
                if periods_quant.is_integer():
                    inputsignalpoints = np.tile(inputsignalpoints, int(periods_quant))
                else:
                    inputsignalpoints = np.tile(inputsignalpoints, int(np.floor(periods_quant) + 1))
                    indexlimit = int(1000 * periods_quant)
                    inputsignalpoints = inputsignalpoints[0:indexlimit]
                timepoints = points * 2 * np.pi / self.FInputSignalDoubleSpinBox3_2.value()
            case 'δ Dirac':
                timepoints = [0]
                inputsignalpoints = [1]
            case 'Other':
                t = sp.Symbol('t', real=True)
                expr = parse_expr(
                    correctExpression(self.FuncInputSignalTextEdit4_2.toPlainText().replace('\n', '')),
                    local_dict={'t': t}, transformations=T[:])
                f = sp.lambdify(t, expr, "numpy")
                inputsignalpoints = f(np.linspace(0, 1, 1000))
                if periods_quant.is_integer():
                    inputsignalpoints = np.tile(inputsignalpoints, int(periods_quant))
                else:
                    inputsignalpoints = np.tile(inputsignalpoints, int(np.floor(periods_quant) + 1))
                    indexlimit = int(1000 * periods_quant)
                    inputsignalpoints = inputsignalpoints[0:indexlimit]
                timepoints = points * 2 * np.pi / self.FInputSignalDoubleSpinBox4_2.value()
            case _:
                my_logger.error('CASO DEFAULT EN buildInput')

        return timepoints, inputsignalpoints

    # Validacion de puntos de medicion
    def MeasPointValidation(self, index: int):
        if index == self.ReferenceComboBox.currentIndex():
            self.MeasurPointComboBox.setCurrentIndex(-1)

    def ReferValidation(self, index: int):
        if index == self.MeasurPointComboBox.currentIndex():
            self.ReferenceComboBox.setCurrentIndex(-1)

    def CurrRLCInputSignalComboBox(self, index):    # Combo box de seleccion de señal de entrada
        if index == 1:
            self.InputTypeStackedWidget_2.setCurrentIndex(0)
        elif index == 2 or index == 3:
            self.InputTypeStackedWidget_2.setCurrentIndex(2)
        elif index == 5:
            self.InputTypeStackedWidget_2.setCurrentIndex(3)
        elif index == 4:
            self.InputTypeStackedWidget_2.setCurrentIndex(4)
        else:
            self.InputTypeStackedWidget_2.setCurrentIndex(1)
