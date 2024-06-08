from PySide6.QtWidgets import QSpacerItem, QFontComboBox, QApplication, QTableWidget, QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidgetItem, QLabel, QPushButton, QGridLayout, QSizePolicy
from PySide6.QtGui     import QKeyEvent, QPainter, QPen, QColor, QFont, QPalette, QBrush
from PySide6.QtCore    import Qt, Signal, Slot
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
        
        self.sudoku_widget.winning.connect(self.win)
        
        right_layout = QVBoxLayout(self.central_widget)
        
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
        
        right_layout.addWidget(easy_button)
        right_layout.addWidget(medium_button)
        right_layout.addWidget(hard_button)

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
        
        #<---- Empty Label ---->
        self.winning_label = QLabel("")
        self.winning_label.setBaseSize()
        right_layout.addWidget(self.winning_label)  # Empty label below the difficulty buttons

        #<---- Numbers layout ---->

        number_button_layout = QGridLayout()
        number_button_layout.setSpacing(5)  # Set the spacing between buttons
        number_button_layout.setContentsMargins(0, 0, 0, 0)  # Set the margins around the layout

        number_buttons = []
        for i in range(1, 10):
            button = QPushButton(str(i))
            button.setFixedSize(50, 50)
            number_buttons.append(button)
            number_button_layout.addWidget(button, (i-1)//3, (i-1)%3)

        number_button_widget = QWidget()
        number_button_widget.setLayout(number_button_layout)
        right_layout.addWidget(number_button_widget)  # Number buttons below the empty label

        button_widget = QWidget()
        button_widget.setLayout(right_layout)
        layout.addWidget(button_widget, 0, 1, alignment=Qt.AlignTop)  # All buttons in the right

        #<---- Font changer ---->
        font_changer = QFontComboBox()
        font_changer.currentFontChanged.connect(self.font_changed)
        right_layout.addWidget(font_changer)
        
        
        self.setMinimumSize(1, 1)
        
    def font_changed(self, font):
        font.setPointSize(15)
        self.sudoku_widget.set_font(font)
        self.sudoku_widget.update_table_font()
        
    @Slot()
    def win(self):
        self.winning_label.setText("You win!")
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec())

