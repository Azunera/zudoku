from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PySide6.QtGui     import QKeyEvent, QFont, QBrush, QColor
from PySide6.QtCore    import Qt, Signal, Slot
from SudokuLogic       import Sudoku
from SudokuCell        import SudokuItem
from SudokuEnums       import Game_Statuses, SkColor
from enum              import Enum
import sys

class SudokuTable(QTableWidget):

    def __init__(self, rows, columns, parent=None):
        super().__init__(rows, columns, parent)
        self.focus_cell = None
        self.focus_xy = None
        self.sudoku = parent.sudoku
        self.colors = SkColor
        self.sudoku.generate_sudoku()
        self.sudoku.set_difficulty("Test")
        self.game = Game_Statuses
        self.font = QFont("Arial", 17)
        self.initUI()
        self.playable = True

    def initUI(self):
        self.setFixedSize(450, 450)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setDefaultSectionSize(50)
        self.verticalHeader().setDefaultSectionSize(50)
        self.setStyleSheet("QTableWidget { background-color: white; gridline-color: lightgray; }")
        
        # Setting for the first itme the sudoku items and its numbers
        for x in range(9):
            for y in range(9):
                item = SudokuItem("", x, y)
                item.set_number(self.sudoku.sudoku[x][y])
                item.setFont(self.font)
                self.setItem(x, y, item)

    def update_table_number(self, x, y):
        item = self.item(x, y)
        item.set_number(self.sudoku.sudoku[x][y])
        
        # Update colors based on status
        status = self.sudoku.statuses[x][y]
        item.set_background_color(status)

    
    
    def update_table_font(self):
        '''Updates the fonts of all the numbers on the table'''
        for x in range(9):
            for y in range(9):
                item = self.item(x, y)
                if item is not None:
                    item.setFont(self.font)

    def update_table(self):
        '''Updates all numbers on table with new numbers'''
        for x in range(9):
            for y in range(9):
                item = self.item(x, y)
                item.set_number(self.sudoku.sudoku[x][y])
                status = self.sudoku.statuses[x][y]
                item.set_background_color(status)

    def handleCellClicked(self, row, column):
        if self.sudoku.lives:
            try:
                self.focus_cell.set_background_color(SkColor.WHITE)
            except: 
                pass
            
            self.focus_cell = self.item(row, column)
            
            if not self.sudoku.is_number_correct(row, column, self.focus_cell.text()):
                self.sudoku.statuses[row][column] = SkColor.RED
                self.focus_cell.set_background_color(self.colors.BLUE)

    def mouseDoubleClickEvent(self, event):
        event.ignore()

    def mousePressEvent(self, event):
        event.ignore()
        # Calculating cell location
        x = event.position().toPoint().y() // self.rowHeight(0)
        y = event.position().toPoint().x() // self.columnWidth(0)
        
        self.handleCellClicked(x, y)

    def mouseMoveEvent(self, event):
        event.ignore()
            
    def color_updater(self):
        '''Updates the colors of the sudoku cells'''
        for x in range(9):
            for y in range(9):
                self.item(x, y).set_background_color(self.sudoku.statuses[x][y])
                
        if self.sudoku.statuses[self.focus_cell.x][self.focus_cell.y] == SkColor.WHITE:
            self.item(self.focus_cell.x, self.focus_cell.y).set_background_color(SkColor.BLUE)
            
    def keyPressEvent(self, event: QKeyEvent) -> None:
        event.ignore()
        if not self.focus_cell or self.sudoku.is_number_correct(self.focus_cell.x, self.focus_cell.y, self.focus_cell.text()) or not self.sudoku.lives:
            return

        key = event.text()
        
        if key.isdigit():
            if self.focus_cell.text() == key:
                pass
            
            # Setting the numbers in both the cell and sudoku logical grid.
            self.sudoku.set_number(self.focus_cell.x, self.focus_cell.y, key)
            self.focus_cell.set_number(key)
            
            # Attempts to find wrong numbers for then highlighthem   
            self.sudoku.update_statuses(self.focus_cell.x, self.focus_cell.y, key)
            if not self.sudoku.is_number_correct(self.focus_cell.x, self.focus_cell.y, key):
                self.sudoku.on_life_lost()
                
            self.color_updater()
            
            
            if self.sudoku.check_win():
                self.game_updater.emit(Game_Statuses.VICTORY)

    
    @Slot()
    def playable_toggler(self, status):
        '''
        Sets the playability of the sudoku table. 
        Arg:
            status (bool): True for setting the table playable; False for turning it unplayable
        '''
        self.playable = status
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = SudokuTable(9, 9)
    table.show()
    sys.exit(app.exec())