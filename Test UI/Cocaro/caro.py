# Form implementation generated from reading ui file 'D:\Documents\code\Python\Tdlt\c3\pythonProject1\Test UI\Cocaro\caro.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 681)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 941, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.frame_board = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.frame_board.setContentsMargins(0, 0, 0, 0)
        self.frame_board.setObjectName("frame_board")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 941, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.col = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.col.setObjectName("col")
        self.horizontalLayout.addWidget(self.col)
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.row = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.row.setObjectName("row")
        self.horizontalLayout.addWidget(self.row)
        self.draw = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.draw.setObjectName("draw")
        self.horizontalLayout.addWidget(self.draw)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 969, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "cột"))
        self.label_2.setText(_translate("MainWindow", "hàng"))
        self.draw.setText(_translate("MainWindow", "draw"))
