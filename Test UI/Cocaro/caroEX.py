from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QPen
from caro import Ui_MainWindow

class caroEX(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Thiết lập UI

        # Thiết lập nút vẽ để vẽ bàn cờ khi nhấn vào
        self.draw.clicked.connect(self.draw_board)
        self.coll = 0  # Số cột
        self.roww = 0  # Số hàng

    def draw_board(self):
        # Lấy số hàng và cột từ các ô nhập
        try:
            self.coll = int(self.col.text())
            self.roww = int(self.row.text())
        except ValueError:
            # Nếu nhập không hợp lệ, dừng và không vẽ gì
            return

        # Làm mới widget để kích hoạt lại paintEvent
        self.frame_board.update()

    def paintEvent(self, event):
        # Kiểm tra nếu col hoặc row bằng 0, không vẽ gì
        if self.coll == 0 or self.roww == 0:
            return

        # Bắt đầu vẽ trên frame_board
        painter = QPainter(self.frame_board)
        painter.setPen(QPen(Qt.GlobalColor.black, 1, Qt.PenStyle.SolidLine))

        # Tính toán kích thước ô
        frame_rect = self.frame_board.rect()
        cell_width = frame_rect.width() // self.coll
        cell_height = frame_rect.height() // self.roww

        # Vẽ các dòng của bảng
        for i in range(self.coll + 1):
            x = i * cell_width
            painter.drawLine(x, 0, x, frame_rect.height())

        for j in range(self.roww + 1):
            y = j * cell_height
            painter.drawLine(0, y, frame_rect.width(), y)

        painter.end()


import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = caroEX()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
