from PyQt6.QtWidgets import QMainWindow
from usdtovnd import Ui_MainWindow

class usdtovndEXT (Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.pushButton.clicked.connect(self.convert)

    def convert(self):
        usd = float(self.lineEdit.text())
        self.label_3.setText(f'{usd * 23520: .2f}')

import sys
from PyQt6.QtWidgets import QApplication, QDialog


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = usdtovndEXT()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())