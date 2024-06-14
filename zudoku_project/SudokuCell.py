from PySide6.QtWidgets import  QTableWidgetItem
from PySide6.QtGui import QColor, QFont, QBrush
from PySide6.QtCore import Qt  
from SudokuEnums import SkColor

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

    def set_background_color(self, status: SkColor):
        match status:
            case SkColor.WHITE:
                self.setBackground(QColor(0, 0, 0))
            case SkColor.RED:
                self.setBackground(QColor(55, 0, 0))
            case SkColor.BLUE:
                self.setBackground(QColor(0, 0, 55))