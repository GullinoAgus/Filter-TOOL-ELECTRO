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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(1, 0, 791, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Filtro = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Filtro.setObjectName("Filtro")
        self.Filtro.addItem("")
        self.Filtro.addItem("")
        self.gridLayout.addWidget(self.Filtro, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.gridLayoutWidget)
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.groupBox = QtWidgets.QGroupBox(self.page_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 223, 134))
        self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 113, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 55, 18))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(70, 70, 84, 34))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 2, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.Filtro.activated['int'].connect(self.stackedWidget.setCurrentIndex) # type: ignore
        self.pushButton.clicked.connect(self.Clickeadoelbot)  # type: ignore
        MainWindow.setTabOrder(self.Filtro, self.lineEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Filtro.setPlaceholderText(_translate("MainWindow", "Holiwi"))
        self.Filtro.setItemText(0, _translate("MainWindow", "sssss"))
        self.Filtro.setItemText(1, _translate("MainWindow", "ddddd"))
        self.groupBox.setTitle(_translate("MainWindow", "Filtrito"))
        self.label.setText(_translate("MainWindow", "xd"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def Clickeadoelbot(self):
        print("hola")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
