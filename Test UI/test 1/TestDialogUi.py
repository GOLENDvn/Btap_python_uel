from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("TestUI.ui")
app = QApplication([])

window = Window()
form = Form()
form.setupUi(window)

def solve():
    a=form.boxa.value()
    b=form.boxb.value()
    dapan=a+b
    form.dapan.setText(str(f"= {dapan}"))

form.nutbam.clicked.connect(solve)

window.show()
app.exec()


