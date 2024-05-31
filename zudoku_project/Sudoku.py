from PySide6.QtWidgets import QApplication, QTableWidget, QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidgetItem, QLabel, QPushButton, QGridLayout, QSizePolicy
from PySide6.QtGui     import QKeyEvent, QPainter, QPen, QColor, QFont, QPalette, QBrush
from PySide6.QtCore    import Qt 
from SudokuLogic       import Sudoku 
from SudokuCell        import SudokuItem
from SudokuWidget      import SudokuTable
import sys

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setWindowTitle("Sudoku") 
        
        self.central_widget = QWidget() 
        self.setCentralWidget(self.central_widget)
        
        layout = QVBoxLayout(self.central_widget)

        easy_button = DifficultyButton('Easy', 'Cyan')
        medium_button = DifficultyButton('Medium', 'Yellow')
        hard_button = DifficultyButton('Hard', 'Red')
        layout.addWidget(easy_button)
        layout.addWidget(medium_button)
        layout.addWidget(hard_button)
        
        sudoku = Sudoku()
        self.sudoku_widget = SudokuTable(9,9)
        layout.addWidget(self.sudoku_widget)
        
        def easy_sudoku():
            sudoku.difficulty('Easy')
            self.sudoku_widget.create_cells(True)
            sudoku.print_sudoku()
            
        def medium_sudoku():
            sudoku.difficulty('Medium')
            self.sudoku_widget.create_cells(True)
            sudoku.print_sudoku()
            
        def hard_sudoku():
            sudoku.difficulty('Hard')
            self.sudoku_widget.create_cells(True)
            sudoku.print_sudoku()
            
        easy_button.clicked.connect(easy_sudoku)
        medium_button.clicked.connect(medium_sudoku)
        hard_button.clicked.connect(hard_sudoku)
        
        self.setMinimumSize(1, 1)
        
class DifficultyButton(QPushButton):
    def __init__(self, difficulty, color):
        super().__init__(difficulty)
        self.dif=difficulty
        self.setFixedWidth(100)
        self.setStyleSheet(f'background-color: {color}')
        self.clicked.emit()
        
        
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     table = SudokuTable(9, 9)
#     table.show()
#     sys.exit(app.exec())
    
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec())

