        # self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        
        # self.grid_size = 9
        # self.cell_size = 50


    # def draw_grid(self):     

    #     cell_size1 = getattr(self, 'cell_size1', None)
        
    #     if cell_size1 is not None and cell_size1 != cell_size:
    #         # self.create_cells()
    #         # self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
    #         # self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
    #         pass
    #     cell_size1 = cell_size
        
    #     painter = QPainter(self)
    #     painter.setRenderHint(QPainter.Antialiasing)
    #     pen = QPen()
    #     pen.setWidth(2)
    #     painter.setPen(pen)

    #     for i in range(10):
    #         if i % 3 == 0:
    #             pen.setWidth(2)
    #         else:
    #             pen.setWidth(1)
    #         painter.setPen(pen)
    #         painter.drawLine(0, i * cell_size, cell_size*9, i * cell_size) 
    #         painter.drawLine(i * cell_size, 0, i * cell_size, cell_size*9)

    # def font_changed(self, font):
        
    # def create_cells(self, update= False):
    #     cell_size = min(self.width(), self.height()) / 9
    #     for x in range(0,9):
    #         for y in range(0,9):
    #             cell = self.findChild(SudokuCell, f"cell_{x}_{y}")

    #             if cell is None:
    #                 cell = SudokuCell(self, self.sudoku.sudoku[x][y], x, y)
    #                 cell.set_target(self.sudoku_o[x][y])
    #                 cell.setObjectName(f"cell_{x}_{y}")
    #                 self.layout.addWidget(cell, x, y)
                    
    #             if update:
    #                 sudoku_o = self.sudoku.sudoku_o[x][y]
    #                 cell.set_target(sudoku_o)
    #                 cell.set_number(self.sudoku.sudoku[x][y])
                    
    #             # mid_x = y * cell_size
    #             # mid_y = x * cell_size

    #             # cell.set_number(cell.text())
                
    #             # cell.setAlignment(Qt.AlignCenter)

    #             # cell.setGeometry(mid_x, mid_y, cell_size, cell_size)
                
    #             cell.setFixedSize(cell_size, cell_size)
                # cell.setFont(QFont('Arial', cell_size/2))
    #             for n in range(9):
    #                 self.layout.setColumnStretch(n,0)
    #                 self.layout.setRowStretch(n, 0)
    #             # cell.show() 
            
    # # def resizeEvent(self, event):
    # #     cell_size = min(self.width(), self.height()) / 9
    # #     self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
