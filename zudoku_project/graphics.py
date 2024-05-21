import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QSizePolicy
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QPalette
from PySide6.QtCore import Qt 
from logic import randomgenerator, difficulty, check_2
from copy import deepcopy

class Sudoku():
    def __init__(self):
        self.sudoku= [[" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "]]

    def setnumber(self, number, x, y):
        if self.sudoku[x][y] == " ":
            self.sudoku[x][y] = number
        else:
            print(f'Failed setting the number {number} in the position {x}/{y}')


    def difficulty(self, dif):
        self.sudoku_o = randomgenerator()
        self.sudoku = difficulty(deepcopy(self.sudoku_o), dif)

    def winner_check(self):
        for row in range(9):
            for number in range(9):
                if self.sudoku[row][number] == " ":
                    return True
        return False
    
    def print_sudoku(self):
        board = self.sudoku
        print(f'''
     1   2   3   4   5   6   7   8   9 
   \033[1m+---+---+---+---+---+---+---+---+---+\033[0m
A  \033[1m|\033[0m {board[0][0]} | {board[0][1]} | {board[0][2]} \033[1m|\033[0m {board[0][3]} | {board[0][4]} | {board[0][5]} \033[1m|\033[0m {board[0][6]} | {board[0][7]} | {board[0][8]} \033[1m|\033[0m
   \033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
B  \033[1m|\033[0m {board[1][0]} | {board[1][1]} | {board[1][2]} \033[1m|\033[0m {board[1][3]} | {board[1][4]} | {board[1][5]} \033[1m|\033[0m {board[1][6]} | {board[1][7]} | {board[1][8]} \033[1m|\033[0m
   \033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
C  \033[1m|\033[0m {board[2][0]} | {board[2][1]} | {board[2][2]} \033[1m|\033[0m {board[2][3]} | {board[2][4]} | {board[2][5]} \033[1m|\033[0m {board[2][6]} | {board[2][7]} | {board[2][8]} \033[1m|\033[0m
   \033[1m+---+---+---+---+---+---+---+---+---+\033[0m
D  \033[1m|\033[0m {board[3][0]} | {board[3][1]} | {board[3][2]} \033[1m|\033[0m {board[3][3]} | {board[3][4]} | {board[3][5]} \033[1m|\033[0m {board[3][6]} | {board[3][7]} | {board[3][8]} \033[1m|\033[0m
   \033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
E  \033[1m|\033[0m {board[4][0]} | {board[4][1]} | {board[4][2]} \033[1m|\033[0m {board[4][3]} | {board[4][4]} | {board[4][5]} \033[1m|\033[0m {board[4][6]} | {board[4][7]} | {board[4][8]} \033[1m|\033[0m
   \033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
F  \033[1m|\033[0m {board[5][0]} | {board[5][1]} | {board[5][2]} \033[1m|\033[0m {board[5][3]} | {board[5][4]} | {board[5][5]} \033[1m|\033[0m {board[5][6]} | {board[5][7]} | {board[5][8]} \033[1m|\033[0m
   \033[1m+---+---+---+---+---+---+---+---+---+\033[0m
G  \033[1m|\033[0m {board[6][0]} | {board[6][1]} | {board[6][2]} \033[1m|\033[0m {board[6][3]} | {board[6][4]} | {board[6][5]} \033[1m|\033[0m {board[6][6]} | {board[6][7]} | {board[6][8]} \033[1m|\033[0m
   \033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
H  \033[1m|\033[0m {board[7][0]} | {board[7][1]} | {board[7][2]} \033[1m|\033[0m {board[7][3]} | {board[7][4]} | {board[7][5]} \033[1m|\033[0m {board[7][6]} | {board[7][7]} | {board[7][8]} \033[1m|\033[0m
   \033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
I  \033[1m|\033[0m {board[8][0]} | {board[8][1]} | {board[8][2]} \033[1m|\033[0m {board[8][3]} | {board[8][4]} | {board[8][5]} \033[1m|\033[0m {board[8][6]} | {board[8][7]} | {board[8][8]} \033[1m|\033[0m
   \033[1m+---+---+---+---+---+---+---+---+---+\033[0m
''')
        
        
class SudokuWidget(QWidget):
    def __init__(self, sudoku):
        super().__init__()
        # self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.sudoku = sudoku
        self.sudoku_o = deepcopy(self.sudoku.sudoku)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(palette)

        self.layout = QGridLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.create_cells()
        
    def paintEvent(self, event):
        self.draw_grid()

    def draw_grid(self):     
        cell_size = min(self.width(), self.height()) / 9
        
        cell_size1 = getattr(self, 'cell_size1', None)
        
        if cell_size1 is not None and cell_size1 != cell_size:
            self.create_cells()
            # self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
            # self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
    
        self.cell_size1 = cell_size
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen()
        pen.setWidth(2)
        painter.setPen(pen)

        for i in range(10):
            if i % 3 == 0:
                pen.setWidth(2)
            else:
                pen.setWidth(1)
            painter.setPen(pen)
            painter.drawLine(0, i * cell_size, cell_size*9, i * cell_size) 
            painter.drawLine(i * cell_size, 0, i * cell_size, cell_size*9)

            
    def create_cells(self, update= False):
        cell_size = min(self.width(), self.height()) / 9
        for x in range(0,9):
            for y in range(0,9):
                cell = self.findChild(SudokuCell, f"cell_{x}_{y}")

                if cell is None:
                    cell = SudokuCell(self, self.sudoku.sudoku[x][y], x, y)
                    cell.set_target(self.sudoku_o[x][y])
                    cell.setObjectName(f"cell_{x}_{y}")
                    self.layout.addWidget(cell, x, y)
                    
                if update:
                    sudoku_o = self.sudoku.sudoku_o[x][y]
                    cell.set_target(sudoku_o)
                    cell.set_number(self.sudoku.sudoku[x][y])
                    
                # mid_x = y * cell_size
                # mid_y = x * cell_size

                # cell.set_number(cell.text())
                
                # cell.setAlignment(Qt.AlignCenter)

                # cell.setGeometry(mid_x, mid_y, cell_size, cell_size)
                
                cell.setFixedSize(cell_size, cell_size)
                cell.setFont(QFont('Arial', cell_size/2))
                for n in range(9):
                    self.layout.setColumnStretch(n,0)
                    self.layout.setRowStretch(n, 0)
                # cell.show() 
            
    # def resizeEvent(self, event):
    #     cell_size = min(self.width(), self.height()) / 9
    #     self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

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
        self.sudoku_widget = SudokuWidget(sudoku)
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
        
    
class SudokuCell(QLabel):
    def __init__(self, parent, number, x, y):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        # self.setFont(QFont("Arial", 20))
        # self.setFixedSize(50, 50)  
        self.set_number(number)
        self.x = x
        self.y = y 
        self.parent = parent
    
    def set_target(self, sudoku_o):
        self.sudoku_o = sudoku_o
        
    def get_target(self):
        return self.sudoku_o 
        
    def set_number(self, number):
        if number == 0:
            number = " " 
        self.setText(str(number))
        
    def mousePressEvent(self, event):
        if self.sudoku_o != self.text():
            try:
                for e in SudokuCell.prevcells:
                    celly = self.parent.findChild(SudokuCell, f"cell_{e[0]}_{e[1]}")
                    celly.colorize_background(Decolorize= True)
            except: 
                pass # This is to avoid the first run-time, when prevcells doesn't exist
                
                SudokuCell.prevcells= []
            
            self.colorize_background(Main= True)
            SudokuCell.prevcells.append([self.x, self.y])
            
             # Colorizing horizontal and vertical adjecent lines
            for n in range(9):
                if n != self.x:
                    celly = self.parent.findChild(SudokuCell, f"cell_{n}_{self.y}")
                    celly.colorize_background()
                    SudokuCell.prevcells.append([celly.x, celly.y])
                    
                if n != self.y:
                    celly = self.parent.findChild(SudokuCell, f"cell_{self.x}_{n}")
                    celly.colorize_background()
                    SudokuCell.prevcells.append([celly.x, celly.y])
                    
            self.setFocus()

    def colorize_background(self, Main= False, Decolorize= False, Wrong=False, cordss= ""):
        self.setAutoFillBackground(True)
        palette = self.palette()
        if Wrong:
            palette.setColor(self.backgroundRole(), QColor(240, 0, 0))
        else:
            if Decolorize:
                self.setAutoFillBackground(False)
            else:
                if not Main:
                    palette.setColor(self.backgroundRole(), QColor('#CFE8F6'))
                    
                else:
                    palette.setColor(self.backgroundRole(), QColor('#9ACEEB'))

        self.setPalette(palette)
    
            
    def keyPressEvent(self, event):
        # Checking number and colorizing
        if self.sudoku_o != self.text():
            key = event.text()
            
            if key.isdigit() and 1 <= int(key) <= 9:
                if self.parent.sudoku.sudoku_o[self.x][self.y] == key:
                    self.setStyleSheet("color: rgb(0, 0, 150);")
                    self.setText(key)
                elif key != self.text():
                    self.setStyleSheet("color: rgb(200, 0, 0);")
                    self.setText(key)
                    wrong_spots= check_2(self.parent.sudoku.sudoku, key, self.x, self.y)
                    for cords in wrong_spots:
                        celly = self.parent.findChild(SudokuCell, f"cell_{cords[0]}_{cords[1]}")
                        # print(cords, celly, cords[0], cords[1])
                        celly.colorize_background(Wrong= True, cordss= wrong_spots)
                    
                    
                else:
                    self.setText("")
                                 
            elif key == '0':
                self.clear_text_signal.emit()

    def clear_text(self):
        self.setText('')
 
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec())