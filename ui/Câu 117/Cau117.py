# Form implementation generated from reading ui file 'D:\Documents\code\Python\Tdlt\c3\pythonProject1\ui\Cau117.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 181, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 80, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 150, 241, 21))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: yellow")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 230, 93, 28))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close) # type: ignore
        self.lineEdit.textChanged['QString'].connect(self.label_2.setText) # type: ignore
        self.pushButton_2.clicked.connect(lambda: self.change_color(Dialog))  # Kết nối nút với hàm change_color
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "exit"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:14pt;\">Signals &amp; Slots</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Change Color"))

    def change_color(self, Dialog):
        Dialog.setStyleSheet("background-color: red")


import sys
from PyQt6.QtWidgets import QApplication, QDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
