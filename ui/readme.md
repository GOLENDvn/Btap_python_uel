Code để chạy file .py đã được tạo từ file .ui

        Dialog

import sys
from PyQt6.QtWidgets import QApplication, QDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())



        main window

import sys
from PyQt6.QtWidgets import QApplication, QDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

        main window (kế thừa)
from PyQt6.QtWidgets import QMainWindow
from //tên_file//.py import Ui_MainWindow

class usdtovndEXT (Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = //tên_file_kế_thừa//()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())




