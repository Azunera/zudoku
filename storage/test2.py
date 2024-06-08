from PySide6.QtWidgets import QApplication, QTableWidget, QMainWindow, QWidget, QVBoxLayout, QTableWidgetItem, QLabel, QPushButton, QGridLayout, QSizePolicy
from PySide6.QtGui import QKeyEvent, QPainter, QPen, QColor, QFont, QPalette, QBrush
from PySide6.QtCore import Qt
from SudokuLogic import Sudoku
from SudokuCell import SudokuItem
from SudokuWidget import SudokuTable
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
        layout.addWidget(self.sudoku_widget, 0, 0)  # Sudoku table on the left

        easy_button = DifficultyButton('Easy', 'Cyan')
        medium_button = DifficultyButton('Medium', 'Yellow')
        hard_button = DifficultyButton('Hard', 'Red')

        button_layout = QVBoxLayout()
        button_layout.addWidget(easy_button)
        button_layout.addWidget(medium_button)
        button_layout.addWidget(hard_button)

        empty_label = QLabel("")
        button_layout.addWidget(empty_label)  # Empty label below the difficulty buttons

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
        button_layout.addWidget(number_button_widget)  # Number buttons below the empty label

        button_widget = QWidget()
        button_widget.setLayout(button_layout)
        layout.addWidget(button_widget, 0, 1, alignment=Qt.AlignTop)  # All buttons in the right

        def easy_sudoku():
            self.sudoku_widget.sudoku.generate_sudoku()
            self.sudoku_widget.sudoku.set_difficulty('Easy')
            self.sudoku_widget.update_table()

        def medium_sudoku():
            self.sudoku_widget.sudoku.generate_sudoku()
            self.sudoku_widget.sudoku.set_difficulty('Medium')
            self.sudoku_widget.update_table()

        def hard_sudoku():
            self.sudoku_widget.sudoku.generate_sudoku()
            self.sudoku_widget.sudoku.set_difficulty('Hard')
            self.sudoku_widget.update_table()

        easy_button.clicked.connect(easy_sudoku)
        medium_button.clicked.connect(medium_sudoku)
        hard_button.clicked.connect(hard_sudoku)

        self.setMinimumSize(1, 1)

class DifficultyButton(QPushButton):
    def __init__(self, difficulty, color):
        super().__init__(difficulty)
        self.dif = difficulty
        self.setFixedWidth(100)
        self.setStyleSheet(f'background-color: {color}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
