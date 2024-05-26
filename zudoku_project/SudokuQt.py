from PySide6.QtWidgets import QApplication, QTableWidget,QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidgetItem, QLabel, QPushButton, QGridLayout, QSizePolicy
from PySide6.QtGui     import QKeyEvent, QPainter, QPen, QColor, QFont, QPalette, QBrush
from PySide6.QtCore    import Qt 
from SudokuClass       import Sudoku 
from SudokuCell        import SudokuItem
import sys

class SudokuTable(QTableWidget):
    def __init__(self, rows, columns, parent=None):
        super().__init__(rows, columns, parent)
        self.focus_cell = None
        self.sudoku = Sudoku()
        self.sudoku.generate_sudoku()
        self.sudoku.set_difficulty("Easy")

        self.initUI()

    def initUI(self):
        self.setFixedSize(450, 450)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setDefaultSectionSize(50)
        self.verticalHeader().setDefaultSectionSize(50)
        
        # # Set background color of the table widget to white
        # self.setStyleSheet("QTableWidget { background-color: white; gridline-color: lightgray; }")
        
        for x in range(9):
            for y in range(9):
                item = SudokuItem("", x, y)
                item.set_number(self.sudoku.sudoku[x][y])
                self.setItem(x, y, item)


        self.cellClicked.connect(self.handleCellClicked)

    def handleCellClicked(self, row, column):
        self.focus_cell = self.item(row, column)
        self.focus_cell.setBackground(QColor(200, 200, 255))
        self.setAutoFillBackground(True)


    def mouseDoubleClickEvent(self, event):
        event.ignore()

    # def mouseReleaseEvent(self, event):
    #     event.ignore()

    def mousePressEvent(self, event):
        event.ignore()
        
    def mouseMoveEvent(self, event):
        event.ignore()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        event.ignore()
        if not self.focus_cell:
            return

        key = event.text()

        if key.isdigit():
            self.focus_cell.set_number(key)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = SudokuTable(9, 9)
    table.show()
    sys.exit(app.exec())

