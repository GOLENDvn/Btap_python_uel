# Form implementation generated from reading ui file 'D:\Documents\code\Python\Tdlt\c3\pythonProject1\ui\Câu 127\Cau127.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 181)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dof = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.dof.setObjectName("dof")
        self.gridLayout.addWidget(self.dof, 0, 1, 1, 1)
        self.convertbutton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.convertbutton.setAutoFillBackground(False)
        self.convertbutton.setCheckable(False)
        self.convertbutton.setAutoDefault(False)
        self.convertbutton.setDefault(True)
        self.convertbutton.setObjectName("convertbutton")
        self.gridLayout.addWidget(self.convertbutton, 1, 1, 1, 1)
        self.doc = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.doc.setText("")
        self.doc.setObjectName("doc")
        self.gridLayout.addWidget(self.doc, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.convertbutton.clicked.connect(self.convert)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Độ F sang độ C"))
        self.convertbutton.setText(_translate("MainWindow", "Convert"))
        self.label_2.setText(_translate("MainWindow", "Fahrenheit (F):"))
        self.label.setText(_translate("MainWindow", "Celsius (C):"))

    def convert (self):
        self.doc.setText(f"{float(self.dof.text())-32/1.8:.2f}")
    
import sys
from PyQt6.QtWidgets import QApplication, QDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())