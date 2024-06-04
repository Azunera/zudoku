from PySide6.QtWidgets import QApplication, QTableWidget,QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidgetItem, QLabel, QPushButton, QGridLayout, QSizePolicy
from PySide6.QtGui     import QKeyEvent, QPainter, QPen, QColor, QFont, QPalette, QBrush
from PySide6.QtCore    import Qt, Slot
from SudokuLogic       import Sudoku 
from SudokuCell        import SudokuItem
import sys

class SudokuTable(QTableWidget):
    def __init__(self, rows, columns, parent=None):
        super().__init__(rows, columns, parent)
        self.focus_cell = None
        self.focus_xy   = None
        self.sudoku = Sudoku()
        self.sudoku.generate_sudoku()
        self.sudoku.set_difficulty("Easy")
        
        self.sudoku.number_set.connect(self.update_table_number)  # Connect signal to slot
        self.font = QFont("Arial", 15)
        
        
        self.initUI()

    def initUI(self):
        self.setFixedSize(450, 450)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setDefaultSectionSize(50)
        self.verticalHeader().setDefaultSectionSize(50)
    
        self.setStyleSheet("QTableWidget { background-color: white; gridline-color: lightgray; }")
        
        for x in range(9):
            for y in range(9):
                item = SudokuItem("", x, y)
                item.set_number(self.sudoku.sudoku[x][y])
                self.setItem(x, y, item)


    def update_table_number(self, x, y):
        item = self.item(x, y)
        item.set_number(self.sudoku.sudoku[x][y])
        # Update color based on status
        status = self.sudoku.statuses[x][y]
        item.set_background_color(status)
        

    def set_font(self, font):
        self.font = font

    def update_table_font(self):
        for x in range(9):
            for y in range(9):
                item = self.item(x, y)
                if item is not None:
                    item.setFont(self.font)

    def update_table(self):
        for x in range(9):
            for y in range(9):
                item = self.item(x, y)
                item.set_number(self.sudoku.sudoku[x][y])
                status = self.sudoku.statuses[x][y]
                item.set_background_color(status)

    def handleCellClicked(self, row, column):
        try:
            print(self.focus_cell.y)
            self.focus_cell.set_background_color(1)
        except: pass
        
        self.focus_cell = self.item(row, column)
        
        if not self.sudoku.is_number_correct(row, column, self.focus_cell.text()):
            self.sudoku.statuses[row][column] = 'F'
            self.focus_cell.set_background_color('F')
            
    def mouseDoubleClickEvent(self, event):
        event.ignore()

    def mousePressEvent(self, event):
        event.ignore()
        # Calculating cell location
        x = event.position().toPoint().y() // self.rowHeight(0)
        y = event.position().toPoint().x() // self.columnWidth(0)
        
        # Handle cell click manually
        self.handleCellClicked(x, y)

    def mouseMoveEvent(self, event):
        event.ignore()
            
    def color_updater(self):
        for x in range(9):
            for y in range(9):
                self.item(x, y).set_background_color(self.sudoku.statuses[x][y])
                
        if self.sudoku.statuses[self.focus_cell.x][self.focus_cell.y] == 1:
            self.item(self.focus_cell.x, self.focus_cell.y).set_background_color('F')
            
            
            
    def keyPressEvent(self, event: QKeyEvent) -> None:
        event.ignore()
        if not self.focus_cell or self.sudoku.is_number_correct(self.focus_cell.x, self.focus_cell.y, self.focus_cell.text()):
            return

        key = event.text()
        
        if key.isdigit():
            if self.focus_cell.text() == key:
                pass
            self.sudoku.set_number(self.focus_cell.x, self.focus_cell.y, key)

            self.sudoku.update_statuses(self.focus_cell.x, self.focus_cell.y, key)
            # print(self.sudoku.statuses)
            self.color_updater()
            

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = SudokuTable(9, 9)
    table.show()
    sys.exit(app.exec())