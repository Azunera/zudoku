#!/usr/bin/env python3
from PySide6.QtWidgets import QSpacerItem, QFontComboBox, QApplication, QTableWidget, QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidgetItem, QLabel, QPushButton, QGridLayout, QSizePolicy
from PySide6.QtGui     import QKeyEvent, QPainter, QPen, QColor, QFont, QPalette, QBrush
from PySide6.QtCore    import Qt, Signal, Slot
from SudokuLogic       import Sudoku 
from SudokuCell        import SudokuItem
from SudokuTable       import SudokuTable
from SudokuEnums       import Game_Statuses
from functools         import partial
from SudokuWidgets     import DifficultyButton
import sys

class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        # Setting intials properties and layouts of the MainWindow
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setWindowTitle("Sudoku") 
        self.central_widget = QWidget() 
        self.setCentralWidget(self.central_widget)
        layout = QGridLayout(self.central_widget)

        # Initialize sudoku logic and board representation
        self.sudoku = Sudoku(self)
        self.table  = SudokuTable(9, 9, self)

        layout.addWidget(self.table, 0, 0)


        # <----->

        self.table.game_updater.connect(self.label_updater)
        self.table.lost_life.connect(self.life_label_setter)
        
        right_layout = QVBoxLayout(self.central_widget)
        
        #<---- Difficulties buttons ---->

      
        easy_button = DifficultyButton('Easy', 'Cyan')
        medium_button = DifficultyButton('Medium', 'Yellow')
        hard_button = DifficultyButton('Hard', 'Red')
        
        right_layout.addWidget(easy_button)
        right_layout.addWidget(medium_button)
        right_layout.addWidget(hard_button)
        
        easy_button.clicked.connect(partial(self.game_reseter, 'Easy'))
        medium_button.clicked.connect(partial(self.game_reseter, 'Medium'))
        hard_button.clicked.connect(partial(self.game_reseter, 'Hard'))

        font = QFont()
        font.setPointSize(16)  
        #<---- Lives Label ---->
        self.lives_label = QLabel("lives left " + str(self.sudoku.lives))
        self.lives_label.setFont(font)
        right_layout.addWidget(self.lives_label)  

        #<---- Game Label ---->
        self.game_label = QLabel("")
        right_layout.addWidget(self.game_label) 
        self.game_label.setFont(font)
        
        #<---- Numbers layout ---->

        number_button_layout = QGridLayout()
        number_button_layout.setSpacing(5)  # Set the spacing between buttons
        number_button_layout.setContentsMargins(0, 0, 0, 0)  # Set the margins around the layout

        number_buttons = []
        for i in range(1, 10):
            button = QPushButton(str(i))
            button.setFixedSize(50, 50)
            button.clicked.connect(partial(self.numbers_pressed, i))
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
        

    def numbers_pressed(self, number):
        event = QKeyEvent(QKeyEvent.KeyPress, 0, Qt.NoModifier, str(number))
        QApplication.postEvent(self.table, event)

    def font_changed(self, font):
        font.setPointSize(17)
        self.table.font = font
        self.table.update_table_font()

    
    def game_reseter(self, difficulty):
        self.sudoku.generate_sudoku()
        self.sudoku.lives_updater(reset=True)
        self.label_updater(Game_Statuses.STATIS)
        self.sudoku.set_difficulty(difficulty)
        self.table.update_table()
        self.life_label_setter(self.sudoku.lives)
        self.sudoku.print_sudoku()
        
    @Slot(Game_Statuses)
    def label_updater(self, status: Game_Statuses):
        match status:
            case Game_Statuses.STATIS:
                self.game_label.setText("")
                
            case Game_Statuses.DEFEAT:
                self.game_label.setText("You lost!")
                
            case Game_Statuses.VICTORY:
                self.game_label.setText("You win!")
                
    @Slot()
    def life_label_setter(self, lives):
        self.lives_label.setText("lives left " + str(lives))
         
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec())

