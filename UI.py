# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1062, 791)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.FilterTools = QtWidgets.QWidget()
        self.FilterTools.setObjectName("FilterTools")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.FilterTools)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.FilterTools)
        self.groupBox.setMaximumSize(QtCore.QSize(400, 400))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FORadio = QtWidgets.QRadioButton(self.groupBox)
        self.FORadio.setChecked(True)
        self.FORadio.setObjectName("FORadio")
        self.horizontalLayout.addWidget(self.FORadio)
        self.SORadio = QtWidgets.QRadioButton(self.groupBox)
        self.SORadio.setObjectName("SORadio")
        self.horizontalLayout.addWidget(self.SORadio)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.FilterTypeStackedWidget = QtWidgets.QStackedWidget(self.groupBox)
        self.FilterTypeStackedWidget.setObjectName("FilterTypeStackedWidget")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.FOComboBox = QtWidgets.QComboBox(self.page_5)
        self.FOComboBox.setObjectName("FOComboBox")
        self.FOComboBox.addItem("")
        self.FOComboBox.addItem("")
        self.FOComboBox.addItem("")
        self.FOComboBox.addItem("")
        self.gridLayout_7.addWidget(self.FOComboBox, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignTop)
        self.FilterTypeStackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.SOComboBox = QtWidgets.QComboBox(self.page_6)
        self.SOComboBox.setObjectName("SOComboBox")
        self.SOComboBox.addItem("")
        self.SOComboBox.addItem("")
        self.SOComboBox.addItem("")
        self.SOComboBox.addItem("")
        self.SOComboBox.addItem("")
        self.SOComboBox.addItem("")
        self.SOComboBox.addItem("")
        self.SOComboBox.addItem("")
        self.gridLayout_8.addWidget(self.SOComboBox, 0, 0, 1, 1)
        self.FilterTypeStackedWidget.addWidget(self.page_6)
        self.verticalLayout_5.addWidget(self.FilterTypeStackedWidget, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 1)
        self.PFSettingsLineEdit = QtWidgets.QLineEdit(self.page_2)
        self.PFSettingsLineEdit.setObjectName("PFSettingsLineEdit")
        self.gridLayout_9.addWidget(self.PFSettingsLineEdit, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.page_7)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.ZFSettingsLineEdit = QtWidgets.QLineEdit(self.page_7)
        self.ZFSettingsLineEdit.setObjectName("ZFSettingsLineEdit")
        self.horizontalLayout_2.addWidget(self.ZFSettingsLineEdit)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_8 = QtWidgets.QLabel(self.page_8)
        self.label_8.setObjectName("label_8")
        self.gridLayout_10.addWidget(self.label_8, 0, 0, 1, 1)
        self.PFSettingsLineEdit2 = QtWidgets.QLineEdit(self.page_8)
        self.PFSettingsLineEdit2.setObjectName("PFSettingsLineEdit2")
        self.gridLayout_10.addWidget(self.PFSettingsLineEdit2, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page_8)
        self.label_9.setObjectName("label_9")
        self.gridLayout_10.addWidget(self.label_9, 1, 0, 1, 1)
        self.ZFSettingsLineEdit2 = QtWidgets.QLineEdit(self.page_8)
        self.ZFSettingsLineEdit2.setObjectName("ZFSettingsLineEdit2")
        self.gridLayout_10.addWidget(self.ZFSettingsLineEdit2, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_8)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.FilterTools)
        self.groupBox_2.setMaximumSize(QtCore.QSize(400, 400))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ISComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.ISComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.ISComboBox.setObjectName("ISComboBox")
        self.ISComboBox.addItem("")
        self.ISComboBox.addItem("")
        self.ISComboBox.addItem("")
        self.ISComboBox.addItem("")
        self.ISComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.ISComboBox)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.InputTypeStackedWidget = QtWidgets.QStackedWidget(self.groupBox_2)
        self.InputTypeStackedWidget.setObjectName("InputTypeStackedWidget")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_13 = QtWidgets.QLabel(self.page_9)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.AInputSignalLineEdit_3 = QtWidgets.QLineEdit(self.page_9)
        self.AInputSignalLineEdit_3.setObjectName("AInputSignalLineEdit_3")
        self.horizontalLayout_4.addWidget(self.AInputSignalLineEdit_3)
        self.InputTypeStackedWidget.addWidget(self.page_9)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.FInputSignalLineEdit = QtWidgets.QLineEdit(self.page_3)
        self.FInputSignalLineEdit.setObjectName("FInputSignalLineEdit")
        self.gridLayout_6.addWidget(self.FInputSignalLineEdit, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 1)
        self.AInputSignalLineEdit = QtWidgets.QLineEdit(self.page_3)
        self.AInputSignalLineEdit.setObjectName("AInputSignalLineEdit")
        self.gridLayout_6.addWidget(self.AInputSignalLineEdit, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.InputTypeStackedWidget.addWidget(self.page_3)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_10)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_14 = QtWidgets.QLabel(self.page_10)
        self.label_14.setObjectName("label_14")
        self.gridLayout_12.addWidget(self.label_14, 0, 0, 1, 1)
        self.AInputSignalLineEdit_2 = QtWidgets.QLineEdit(self.page_10)
        self.AInputSignalLineEdit_2.setObjectName("AInputSignalLineEdit_2")
        self.gridLayout_12.addWidget(self.AInputSignalLineEdit_2, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.page_10)
        self.label_15.setObjectName("label_15")
        self.gridLayout_12.addWidget(self.label_15, 1, 0, 1, 1)
        self.FInputSignalLineEdit_2 = QtWidgets.QLineEdit(self.page_10)
        self.FInputSignalLineEdit_2.setObjectName("FInputSignalLineEdit_2")
        self.gridLayout_12.addWidget(self.FInputSignalLineEdit_2, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.page_10)
        self.label_16.setObjectName("label_16")
        self.gridLayout_12.addWidget(self.label_16, 2, 0, 1, 1)
        self.DCInputSignalLineEdit = QtWidgets.QLineEdit(self.page_10)
        self.DCInputSignalLineEdit.setObjectName("DCInputSignalLineEdit")
        self.gridLayout_12.addWidget(self.DCInputSignalLineEdit, 2, 1, 1, 1)
        self.InputTypeStackedWidget.addWidget(self.page_10)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_11.addWidget(self.label_11, 0, 0, 1, 1)
        self.FuncInputSignalLineEdit = QtWidgets.QLineEdit(self.page_4)
        self.FuncInputSignalLineEdit.setObjectName("FuncInputSignalLineEdit")
        self.gridLayout_11.addWidget(self.FuncInputSignalLineEdit, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout_11.addWidget(self.label_12, 1, 0, 1, 1)
        self.FInputSignalLineEdit_3 = QtWidgets.QLineEdit(self.page_4)
        self.FInputSignalLineEdit_3.setObjectName("FInputSignalLineEdit_3")
        self.gridLayout_11.addWidget(self.FInputSignalLineEdit_3, 1, 1, 1, 1)
        self.InputTypeStackedWidget.addWidget(self.page_4)
        self.gridLayout_4.addWidget(self.InputTypeStackedWidget, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 2, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.gridLayout_13.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.BodePlotBox = QtWidgets.QGroupBox(self.FilterTools)
        self.BodePlotBox.setMinimumSize(QtCore.QSize(300, 300))
        self.BodePlotBox.setObjectName("BodePlotBox")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.BodePlotBox)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.horizontalLayout_6.addWidget(self.BodePlotBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.InputAndOutputBox = QtWidgets.QGroupBox(self.FilterTools)
        self.InputAndOutputBox.setMinimumSize(QtCore.QSize(300, 300))
        self.InputAndOutputBox.setObjectName("InputAndOutputBox")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.InputAndOutputBox)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.horizontalLayout_5.addWidget(self.InputAndOutputBox)
        self.PolesAndZerosBox = QtWidgets.QGroupBox(self.FilterTools)
        self.PolesAndZerosBox.setMinimumSize(QtCore.QSize(300, 300))
        self.PolesAndZerosBox.setMaximumSize(QtCore.QSize(9999999, 999999))
        self.PolesAndZerosBox.setObjectName("PolesAndZerosBox")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.PolesAndZerosBox)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.horizontalLayout_5.addWidget(self.PolesAndZerosBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.gridLayout_13.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.tabWidget.addTab(self.FilterTools, "")
        self.RLCSerie = QtWidgets.QWidget()
        self.RLCSerie.setObjectName("RLCSerie")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.RLCSerie)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.RLCLayout = QtWidgets.QGridLayout()
        self.RLCLayout.setObjectName("RLCLayout")
        self.gridLayout_18.addLayout(self.RLCLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.RLCSerie, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.FilterTypeStackedWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.InputTypeStackedWidget.setCurrentIndex(1)
        self.FORadio.toggled['bool'].connect(MainWindow.FORadioButtonActive) # type: ignore
        self.SORadio.toggled['bool'].connect(MainWindow.SORadioButtonActive) # type: ignore
        self.FOComboBox.activated['int'].connect(MainWindow.CurrFilterComboBox) # type: ignore
        self.ISComboBox.activated['int'].connect(MainWindow.CurrInputComboBox) # type: ignore
        self.pushButton.clicked.connect(MainWindow.EnterTheMatrix) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Settings"))
        self.FORadio.setText(_translate("MainWindow", "First Order"))
        self.SORadio.setText(_translate("MainWindow", "Second Order"))
        self.FOComboBox.setItemText(0, _translate("MainWindow", "Low Pass"))
        self.FOComboBox.setItemText(1, _translate("MainWindow", "High Pass"))
        self.FOComboBox.setItemText(2, _translate("MainWindow", "All Pass"))
        self.FOComboBox.setItemText(3, _translate("MainWindow", "Create new filter"))
        self.SOComboBox.setItemText(0, _translate("MainWindow", "Low Pass"))
        self.SOComboBox.setItemText(1, _translate("MainWindow", "High Pass"))
        self.SOComboBox.setItemText(2, _translate("MainWindow", "All Pass"))
        self.SOComboBox.setItemText(3, _translate("MainWindow", "Band Pass"))
        self.SOComboBox.setItemText(4, _translate("MainWindow", "Notch"))
        self.SOComboBox.setItemText(5, _translate("MainWindow", "Low-Pass Notch"))
        self.SOComboBox.setItemText(6, _translate("MainWindow", "High-Pass Notch"))
        self.SOComboBox.setItemText(7, _translate("MainWindow", "Create new filter"))
        self.label.setText(_translate("MainWindow", "Wo1"))
        self.label_3.setText(_translate("MainWindow", "Wo2"))
        self.label_2.setText(_translate("MainWindow", "Sigma1"))
        self.label_10.setText(_translate("MainWindow", "Sigma2"))
        self.label_6.setText(_translate("MainWindow", "Pole Frecuency"))
        self.label_7.setText(_translate("MainWindow", "Zero Frecuency"))
        self.label_8.setText(_translate("MainWindow", "Pole Frecuency"))
        self.label_9.setText(_translate("MainWindow", "Zero Frecuency"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Input Signal"))
        self.ISComboBox.setItemText(0, _translate("MainWindow", "Cos"))
        self.ISComboBox.setItemText(1, _translate("MainWindow", "Step"))
        self.ISComboBox.setItemText(2, _translate("MainWindow", "Periodic Pulse"))
        self.ISComboBox.setItemText(3, _translate("MainWindow", "Triangle Periodic Pulse"))
        self.ISComboBox.setItemText(4, _translate("MainWindow", "Other"))
        self.label_13.setText(_translate("MainWindow", "Amplitude"))
        self.label_4.setText(_translate("MainWindow", "Frecuency"))
        self.label_5.setText(_translate("MainWindow", "Amplitude"))
        self.label_14.setText(_translate("MainWindow", "Amplitude"))
        self.label_15.setText(_translate("MainWindow", "Frecuency"))
        self.label_16.setText(_translate("MainWindow", "Duty Cycle"))
        self.label_11.setText(_translate("MainWindow", "f(t)"))
        self.label_12.setText(_translate("MainWindow", "Frecuency"))
        self.pushButton.setText(_translate("MainWindow", "Enter the matix"))
        self.BodePlotBox.setTitle(_translate("MainWindow", "Bode Plot"))
        self.InputAndOutputBox.setTitle(_translate("MainWindow", "Input and Output"))
        self.PolesAndZerosBox.setTitle(_translate("MainWindow", "Poles and Zeros"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FilterTools), _translate("MainWindow", "Filter Tools"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RLCSerie), _translate("MainWindow", "RLC serie"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
