#!/usr/bin/env python3
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QSizePolicy, QFontComboBox
from PySide6.QtGui     import QKeyEvent, QFont
from PySide6.QtCore    import Qt, Slot
from SudokuLogic       import Sudoku 
from SudokuTable       import SudokuWidget
from SudokuEnums       import Game_Statuses, SkColor
from functools         import partial
from SudokuWidgets     import DifficultyButton
from enum              import Enum
import sys
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting startings properties and layouts of the MainWindow
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setWindowTitle("Zudoku") 
        self.central_widget = QWidget() 
        self.setCentralWidget(self.central_widget)

        main_layout = QGridLayout(self.central_widget)
        
        # Initialize sudoku logic and board representation
        self.sudoku = Sudoku(self)
        self.table  = SudokuWidget(self)
        main_layout.addWidget(self.table, 0, 0)

        self.setMinimumSize(650,410)

 
       # Load game data if available
        self.load_game()


        # Connecting lives system from Sudoku to lives and gamestatus label.
        self.sudoku.lost_one_life.connect(self.life_label_setter)
        self.sudoku.lost_all_lives.connect(self.label_updater)
        self.sudoku.sudoku_completed.connect(self.label_updater)
        
        # Initializing the right sidebar widget
        right_sidebar_widget = QWidget()
        right_sidebar_layout = QVBoxLayout(right_sidebar_widget)

        # Difficulties buttons
        easy_button = DifficultyButton('Easy', SkColor.EASY_GREEN)
        medium_button = DifficultyButton('Medium', SkColor.MEDIUM_ORANGE)
        hard_button = DifficultyButton('Hard', SkColor.HARD_RED)
        
        right_sidebar_layout.addWidget(easy_button)
        right_sidebar_layout.addWidget(medium_button)
        right_sidebar_layout.addWidget(hard_button)
        
        easy_button.clicked.connect(partial(self.game_reseter, 'Easy'))
        medium_button.clicked.connect(partial(self.game_reseter, 'Medium'))
        hard_button.clicked.connect(partial(self.game_reseter, 'Hard'))
        
        # Lives & Game status labels
        LGfont = QFont()
        LGfont.setPointSize(16) 
        
        self.lives_label = QLabel("lives left " + str(self.sudoku.lives))
        self.lives_label.setFont(LGfont)
        right_sidebar_layout.addWidget(self.lives_label)  

        self.game_label = QLabel("")
        right_sidebar_layout.addWidget(self.game_label) 
        self.game_label.setFont(LGfont)
        
        # Numbers layout
        number_button_layout = QGridLayout()
        number_button_layout.setSpacing(5)  
        number_button_layout.setContentsMargins(0, 0, 0, 0) 

        number_buttons = []
        for i in range(1, 10):
            button = QPushButton(str(i))
            button.setFixedSize(50, 50)
            button.clicked.connect(partial(self.numbers_pressed, i))
            number_buttons.append(button)
            number_button_layout.addWidget(button, (i-1)//3, (i-1)%3)

        number_button_widget = QWidget()
        number_button_widget.setLayout(number_button_layout)
        right_sidebar_layout.addWidget(number_button_widget)

        # Font changer
        self.font_changer = QFontComboBox()
        self.font_changer.currentFontChanged.connect(self.font_changed)
        right_sidebar_layout.addWidget(self.font_changer)

        # Set the right sidebar widget as the layout for the central widget
        main_layout.addWidget(right_sidebar_widget, 0, 1, alignment=Qt.AlignTop)


    def closeEvent(self, event):
        self.save_game()
        super().closeEvent(event)
        
    def numbers_pressed(self, number):
        event = QKeyEvent(QKeyEvent.KeyPress, 0, Qt.NoModifier, str(number))
        if self.table.focus_cell is not None:
            QApplication.postEvent(self.table, event)

    def font_changed(self, font):
        font.setPointSize(17)
        self.table.font = font
        self.table.update()
    
    def game_reseter(self, difficulty):
        # Generates a randomly sudoku, sets its difficulty
        self.sudoku.generate_sudoku()
        self.sudoku.set_difficulty(difficulty)

        # Updates the lives display and current game status
        self.life_label_setter(self.sudoku.lives)
        self.label_updater(Game_Statuses.IN_GAME)

        # Clears table colors 
        self.table.focus_cell = None
        self.table.update()
        
    @Slot(Game_Statuses)
    def label_updater(self, status: Game_Statuses):
        match status:
            case Game_Statuses.IN_GAME:
                self.game_label.setText("")
                
            case Game_Statuses.LOST:
                self.game_label.setText("You lost!")

            case Game_Statuses.COMPLETED:
                self.game_label.setText("You win!")
                
    @Slot()
    def life_label_setter(self, lives):
        self.lives_label.setText("lives left " + str(lives))
    def save_game(self):
        game_data = {
            'sudoku': self.sudoku.sudoku,
            'solution': self.sudoku.solution,
            'statuses': [[[color.name for color in row] for row in column] for column in self.sudoku.statuses],
            'difficulty': self.sudoku.difficulty,
            'lives': self.sudoku.lives,
            'focus_cell': self.table.focus_cell
        }
        with open('sudoku_save.json', 'w') as sufile:
            json.dump(game_data, sufile)

    def load_game(self):
        try:
            with open('sudoku_save.json', 'r') as sufile:
                game_data = json.load(sufile)
                
                self.sudoku.sudoku = game_data['sudoku']
                self.sudoku.solution = game_data.get('solution', None)
                self.sudoku.statuses = [
                    [
                        [SkColor[color] for color in row]
                        for row in column
                    ]
                    for column in game_data['statuses']
                ]
                self.sudoku.difficulty = game_data['difficulty']
                self.sudoku.lives = game_data['lives']
                self.focus_cell = game_data['focus_cell'] if game_data['focus_cell'] else None
                
                print(self.sudoku.statuses)
                self.update() 
        except:
            pass


if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec())
    
    
    