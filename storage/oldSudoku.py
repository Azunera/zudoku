from PySide6.QtWidgets import QSpacerItem, QFontComboBox, QApplication, QTableWidget, QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidgetItem, QLabel, QPushButton, QGridLayout, QSizePolicy
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
        
        layout = QGridLayout(self.central_widget)

        sudoku = Sudoku()
        self.sudoku_widget = SudokuTable(9, 9)
        layout.addWidget(self.sudoku_widget, 0, 0)
        
        # self.sudoku_widget.winning.connect(self.win)
        
        
        right_widgets_layout = QVBoxLayout(self.central_widget)
        layout.addLayout(right_widgets_layout, 0, 1)
        
        spacer = QSpacerItem(40,40)
        
        #<---- Font changer ---->
        font_changer = QFontComboBox()
        font_changer.currentFontChanged.connect(self.font_changed)
        right_widgets_layout.addWidget(font_changer)
    
        right_widgets_layout.addSpacerItem(spacer)
        
        spacer = QSpacerItem(10,10)
        
        #<---- Difficulties buttons ---->
        class DifficultyButton(QPushButton):
            def __init__(self, difficulty, color):
                super().__init__(difficulty)
                self.dif=difficulty
                self.setFixedWidth(100)
                self.setStyleSheet(f'background-color: {color}')
                self.clicked.emit()
        
        easy_button = DifficultyButton('Easy', 'Cyan')
        medium_button = DifficultyButton('Medium', 'Yellow')
        hard_button = DifficultyButton('Hard', 'Red')
        
        right_widgets_layout.addWidget(easy_button)
    
        right_widgets_layout.addSpacerItem(spacer)
        
        right_widgets_layout.addWidget(medium_button)
    
        right_widgets_layout.addSpacerItem(spacer)
        
        right_widgets_layout.addWidget(hard_button)

        right_widgets_layout.addSpacerItem(spacer)
        
        right_widgets_layout.addStretch()
        
        # self.winning_label = QLabel()
        # right_widgets_layout.addWidget(winning_label)
        
        
        def easy_sudoku():            
            self.sudoku_widget.sudoku.generate_sudoku() 
            self.sudoku_widget.sudoku.set_difficulty('Easy')
            self.sudoku_widget.update_table()
            sudoku.print_sudoku()
            
        def medium_sudoku():
            self.sudoku_widget.sudoku.generate_sudoku() 
            self.sudoku_widget.sudoku.set_difficulty('Medium')
            self.sudoku_widget.update_table()
            sudoku.print_sudoku()
            
        def hard_sudoku():
            self.sudoku_widget.sudoku.generate_sudoku() 
            self.sudoku_widget.sudoku.set_difficulty('Hard')
            self.sudoku_widget.update_table()
            sudoku.print_sudoku()
            
        easy_button.clicked.connect(easy_sudoku)
        medium_button.clicked.connect(medium_sudoku)
        hard_button.clicked.connect(hard_sudoku)
        
        self.setMinimumSize(1, 1)
        
    def font_changed(self, font):
        font.setPointSize(15)
        self.sudoku_widget.set_font(font)
        self.sudoku_widget.update_table_font()
    
#     def win(self, status):
#         if status:
#             self.winning_label.setText("You win!")
        
# # if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     table = SudokuTable(9, 9)
#     table.show()
#     sys.exit(app.exec())
    
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec())

