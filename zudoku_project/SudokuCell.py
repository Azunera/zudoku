from PySide6.QtWidgets import  QTableWidgetItem
from PySide6.QtGui import QKeyEvent, QPainter, QPen, QColor, QFont, QPalette, QBrush
from PySide6.QtCore import Qt 
from SudokuLogic import Sudoku 


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
            self.setForeground(QBrush(QColor("black")))
            self.setText(str(number))
        else:
            self.setText("")

    def set_background_color(self, status='Clear'):
        match status:
            case 'Focused':
                self.setBackground(QColor(200, 200, 255))
            case 'Wrong':
                self.setBackground(QColor(255, 200, 200))
            case 'Clear':
                self.setBackground(QColor(255, 255, 255))
            case _:
                self.setBackground(QColor(255, 255, 255))
                