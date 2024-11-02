from PySide6.QtWidgets   import QWidget
from PySide6.QtGui       import QPainter, QPen, QColor, QFont
from PySide6.QtCore      import Qt, QRect
from SudokuEnums         import SkColor



class SudokuWidget(QWidget):

    
    def __init__(self, parent):
        super().__init__(parent)
    
    
        self.sudoku = parent.sudoku
        self.sudoku.generate_sudoku('Medium')
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
                    rect = QRect(col * cell_size + 1, row * cell_size + 1, cell_size - 1, cell_size - 1)
                    
                    # Painting the background 
                    if self.sudoku.statuses[row][col][0] == SkColor.RED:
                        painter.fillRect(rect, QColor(*SkColor.RED.value))
                    elif self.sudoku.statuses[row][col][0] == SkColor.WHITE:
                        painter.fillRect(rect, QColor(*SkColor.WHITE.value))
  
                    # Set the text color
                    if self.sudoku.statuses[row][col][1] == SkColor.WRONG_RED:
                        painter.setPen(QPen(QColor(*SkColor.WRONG_RED.value)))
                    elif self.sudoku.statuses[row][col][1] == SkColor.CORRECT_BLUE:
                        painter.setPen(QPen(QColor(*SkColor.CORRECT_BLUE.value)))
                    else:
                        painter.setPen(QPen(Qt.black))  # Default text color
                        
                    # Finally drawing the number
                    painter.drawText(rect, Qt.AlignCenter, str(self.sudoku.sudoku[row][col]))




    def highlight_focus_cell(self):
        if not self.focus_cell:
            return
        try:
            row, col = self.focus_cell
        except: # Skips if doens't exist
            pass
        # Only check if the cell has focus and if the number is correct or not
        if self.sudoku.is_number_correct(row, col, self.sudoku.sudoku[row][col]) or not self.sudoku.lives:
            return

        painter = QPainter(self)
        cell_size = min(self.width(), self.height()) // 9
        self.font.setPointSize(cell_size / 2.2)
        
        # Defining the highlighting function
        def highlight_cell(row, col, color: SkColor):
            cell_size = min(self.width(), self.height()) // 9
        
            rect = QRect(col * cell_size + 1, row * cell_size + 1, cell_size - 1, cell_size - 1)

            if self.sudoku.statuses[row][col][0] != SkColor.RED or color == SkColor.FOCUS_BLUE:
                painter.fillRect(rect, QColor(*color.value))

            # Redraw the number in the cell if it exists
            if self.sudoku.sudoku[row][col] != " ":
                self.font.setPointSize(cell_size / 2.2)
                painter.setFont(self.font)
                pen_color = self.sudoku.statuses[row][col][1].value
                painter.setPen(QPen(QColor(*pen_color), 2, Qt.SolidLine))
                painter.drawText(rect, Qt.AlignCenter, str(self.sudoku.sudoku[row][col]))

        # Applying it to the desired cells, order matters! 
        for new in range(9):
                highlight_cell(row, new, SkColor.CROSS_BLUE)
                highlight_cell(new, col, SkColor.CROSS_BLUE)
        
        highlight_cell(row, col, SkColor.FOCUS_BLUE)

            
    def update_sudoku(self):
        self.update()
        
    def mousePressEvent(self, event):
        cell_size = min(self.width(), self.height()) // 9
        x = event.position().x() // cell_size
        y = event.position().y() // cell_size
        self.focus_cell = (int(y), int(x))
        try:
            self.update()
        except Exception as ex:
            print(ex)


    def keyPressEvent(self, event):
        if self.focus_cell is None:
            return 
        row, col = self.focus_cell
            
        if self.sudoku.is_number_correct(row, col, self.sudoku.sudoku[row][col]) or not self.sudoku.lives:
            return

        if event.text().isdigit() and event.text() != "0":
            number = event.text()
            row, col = self.focus_cell
            self.sudoku.sudoku[row][col] = str(number) if number != self.sudoku.sudoku[row][col] else " "

            # Attempts to find wrong numbers for then highlighthem   
            self.sudoku.update_statuses(row, col, number)
            if not self.sudoku.is_number_correct(row, col, number):
                self.sudoku.statuses[row][col][1] = SkColor.WRONG_RED
                self.sudoku.on_life_lost()
            else:
                self.sudoku.statuses[row][col][1] = SkColor.CORRECT_BLUE

            self.sudoku.check_win()

            self.update()



