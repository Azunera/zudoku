from PySide6.QtWidgets import  QTableWidgetItem
from PySide6.QtGui import QKeyEvent, QPainter, QPen, QColor, QFont, QPalette, QBrush
from PySide6.QtCore import Qt 
from SudokuClass import Sudoku 


class SudokuItem(QTableWidgetItem):
    def __init__(self, number="", x=0, y=0):
        super().__init__(number)
        self.setTextAlignment(Qt.AlignCenter)
        self.setFont(QFont("Arial", 20))
        self.x = x
        self.y = y
        self.set_number(number)

    def set_number(self, number):
        if number:
            # self.setForeground(QBrush(QColor("black")))
            self.setText(str(number))
        else:
            self.setText("")

    def mouseDoubleClickEvent(self, event):
        event.ignore()

    def mouseReleaseEvent(self, event):
        event.ignore()

    def mousePressEvent(self, event):
        event.ignore()

    def mouseMoveEvent(self, event):
        event.ignore()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        event.ignore()