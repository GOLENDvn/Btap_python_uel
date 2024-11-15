# Form implementation generated from reading ui file 'D:\Documents\code\Python\Tdlt\c3\pythonProject1\ui\Câu 128\Cau128.ui'
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
        MainWindow.resize(441, 181)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.gridGroupBox.setGeometry(QtCore.QRect(10, 0, 411, 121))
        self.gridGroupBox.setTabletTracking(False)
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.convertbutton = QtWidgets.QPushButton(parent=self.gridGroupBox)
        self.convertbutton.setObjectName("convertbutton")
        self.gridLayout.addWidget(self.convertbutton, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridGroupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.nam_duong = QtWidgets.QLineEdit(parent=self.gridGroupBox)
        self.nam_duong.setObjectName("nam_duong")
        self.gridLayout.addWidget(self.nam_duong, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridGroupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nam_am = QtWidgets.QLabel(parent=self.gridGroupBox)
        self.nam_am.setText("")
        self.nam_am.setObjectName("nam_am")
        self.gridLayout.addWidget(self.nam_am, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 26))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Lịch dương sang âm"))
        self.convertbutton.setText(_translate("MainWindow", "Chuyển"))
        self.label_2.setText(_translate("MainWindow", "Năm âm lịch"))
        self.label.setText(_translate("MainWindow", "Nhập năm dương lịch"))
    def convert(self):
        try:
            year = int(self.nam_duong.text())

            can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
            chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

            can_index = (year + 6) % 10
            chi_index = (year + 8) % 12
            self.nam_am.setStyleSheet("color: black")
            self.nam_am.setText(f"{can[can_index]} {chi[chi_index]}")
        except ValueError:
            self.nam_am.setStyleSheet("color: red")
            self.nam_am.setText("Vui lòng nhập năm hợp lệ!")

import sys
from PyQt6.QtWidgets import QApplication, QDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
