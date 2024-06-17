from PySide6.QtWidgets   import QWidget
from PySide6.QtGui       import QPainter, QPen, QColor, QFont, QPalette
from PySide6.QtCore      import Qt, QRect, Slot
from SudokuEnums         import SkColor

class SudokuWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.sudoku = parent.sudoku
        self.sudoku.generate_sudoku()
        self.sudoku.set_difficulty("Medium")
        self.colors = SkColor
        self.setMinimumSize(400,400)
        # self.sudoku.number_set.connect(self.update_table_number)  # Connect signal to slot

        self.setAutoFillBackground(True)


        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(palette)


        self.font = QFont()
        self.font.setFamilies(['Arial', 'Helvetica', 'Sans-serif'])  # List of alternative fonts
       
        self.focus_cell = None  # To keep track of the selected cell

        self.setFocusPolicy(Qt.StrongFocus)
    def paintEvent(self, event):
        self.draw_numbers_and_colors()
        self.draw_grid()
        if self.focus_cell:
            self.highlight_focus_cell()


    def set_font(self, font):
        self.font = font
        self.update()


    def draw_grid(self):
        cell_size = min(self.width(), self.height()) // 9
        painter = QPainter(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
       
        # Draw the grid lines
        for i in range(10):
            if i % 3 == 0:
                pen.setWidth(2)
            else:
                pen.setWidth(1)
            painter.setPen(pen)
           
            painter.drawLine(0, i * cell_size, cell_size * 9, i * cell_size)
            painter.drawLine(i * cell_size, 0, i * cell_size, cell_size * 9)

    def draw_numbers_and_colors(self):
        # self.sudoku.print_sudoku()
           
        cell_size = min(self.width(), self.height()) // 9
        painter = QPainter(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
       
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
            self.update()
                        
            # self.color_updater()
                    
            # if self.sudoku.check_win():
            #     self.game_updater.emit(Game_Statuses.VICTORY)

    @Slot()
    def playable_toggler(self, status):
        '''
        Sets the playability of the sudoku table. 
        Arg:
            status (bool): True for setting the table playable; False for turning it unplayable
        '''
        self.playable = status




