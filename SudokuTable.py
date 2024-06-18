from PySide6.QtWidgets   import QWidget
from PySide6.QtGui       import QPainter, QPen, QColor, QFont
from PySide6.QtCore      import Qt, QRect
from SudokuEnums         import SkColor
import json


class SudokuWidget(QWidget):

    
    def __init__(self, parent):
        super().__init__(parent)
    
    
        self.sudoku = parent.sudoku
        self.sudoku.generate_sudoku()
        self.sudoku.set_difficulty("Test")
        self.setMinimumSize(400,400)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(palette)

        self.font = QFont()
        self.font.setFamilies(['Arial', 'Helvetica', 'Sans-serif'])  

        self.focus_cell = None  

        # Letting keyPressEvent work
        self.setFocusPolicy(Qt.StrongFocus) 


    def paintEvent(self, event):
        painter = QPainter(self)
        cell_size = min(self.width(), self.height()) // 9
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)

        self.draw_numbers_and_colors(painter, cell_size, pen)
        self.draw_grid(painter, cell_size, pen)

        if self.focus_cell:
            self.highlight_focus_cell()


    def draw_grid(self, painter, cell_size, pen):
        for i in range(10):
            if i % 3 == 0:
                pen.setWidth(2)
            else:
                pen.setWidth(1)
            painter.setPen(pen)
           
            painter.drawLine(0, i * cell_size, cell_size * 9, i * cell_size)
            painter.drawLine(i * cell_size, 0, i * cell_size, cell_size * 9)


    def draw_numbers_and_colors(self, painter, cell_size, pen):
        self.font.setPointSize(cell_size / 2.2)
        painter.setFont(self.font)
       
        for row in range(9):
            for col in range(9):
                if self.sudoku.sudoku[row][col] != " ":
                    rect = QRect(col * cell_size+1, row * cell_size+1, cell_size-1, cell_size-1)
                    if self.sudoku.statuses[row][col] == SkColor.RED:
                        painter.fillRect(rect, QColor(255, 200, 200))  
                    elif self.sudoku.statuses[row][col] == SkColor.WHITE:
                        painter.fillRect(rect, QColor(255, 255, 255)) 
                    painter.drawText(rect, Qt.AlignCenter, str(self.sudoku.sudoku[row][col]))


    def save_game(self):
        game_data = {
            'sudoku': self.sudoku.sudoku,
            'statuses': [[status.name for status in row] for row in self.sudoku.statuses],
            'difficulty': self.sudoku.difficulty,
            'lives': self.sudoku.lives,
            'focus_cell': self.focus_cell
        }
        with open('sudoku_save.json', 'w') as sufile:
            json.dump(game_data, sufile)

    def load_game(self):
        try:
            with open('sudoku_save.json', 'r') as sufile:
                game_data = json.load(sufile)
                self.sudoku.sudoku = game_data['sudoku']
                self.sudoku.statuses = [[SkColor[status] for status in row] for row in game_data['statuses']]
                self.sudoku.statuses = game_data['statuses']
                self.sudoku.difficulty = game_data['difficulty']
                self.sudoku.lives = game_data['lives']
                self.focus_cell = tuple(game_data['focus_cell']) if game_data['focus_cell'] else None
                self.update()
        except:
            pass  # No saved game file found

    def highlight_focus_cell(self):
        row, col = self.focus_cell
        if self.sudoku.is_number_correct(row, col, self.sudoku.sudoku[row][col]) or not self.sudoku.lives:
            return
        if self.focus_cell:
            painter = QPainter(self)
            cell_size = min(self.width(), self.height()) // 9
            row, col = self.focus_cell
            rect = QRect(col * cell_size+1, row * cell_size+1, cell_size-1.5, cell_size-1)
            # Fill the selected cell with a blue color
            painter.fillRect(rect, QColor(200, 200, 255))  # Light blue background

            # Redraw the number in the cell if it exists
            if self.sudoku.sudoku[row][col] != " ":
                self.font.setPointSize(cell_size / 2.2)
                painter.setFont(self.font)
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawText(rect, Qt.AlignCenter, str(self.sudoku.sudoku[row][col]))
                
    def update_sudoku(self):
        self.update()
        
    def mousePressEvent(self, event):
        cell_size = min(self.width(), self.height()) // 9
        x = event.position().x() // cell_size
        y = event.position().y() // cell_size
        self.focus_cell = (int(y), int(x))
        self.update()


    def keyPressEvent(self, event):
        row, col = self.focus_cell
        if self.sudoku.is_number_correct(row, col, self.sudoku.sudoku[row][col]) or not self.sudoku.lives:
            return

        if self.focus_cell and event.text().isdigit() and event.text() != "0":
            number = event.text()
            row, col = self.focus_cell
            self.sudoku.sudoku[row][col] = str(number) if number != self.sudoku.sudoku[row][col] else " "

            # Attempts to find wrong numbers for then highlighthem   
            self.sudoku.update_statuses(row, col, number)
            if not self.sudoku.is_number_correct(row, col, number):
                self.sudoku.on_life_lost()

            self.sudoku.check_win()

            self.update()



