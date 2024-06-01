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
        self.setForeground(QBrush(QColor("blue")))
        
    def set_number(self, number):
        if number:
            self.setText(str(number))

    def set_background_color(self, status):
        match status:
            case 1:
                self.setBackground(QColor(255, 255, 255))
            case -1:
                self.setBackground(QColor(255, 200, 200))
            case 'F':
                self.setBackground(QColor(200, 200, 255))

