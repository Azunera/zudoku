# REMOVE SIGNAL AND INSTEAD YK

from random import shuffle, sample
from copy import deepcopy
from enum import Enum
from PySide6.QtCore import QObject, Signal
from SudokuEnums import SkColor, Game_Statuses

class Sudoku(QObject):
    lost_one_life   = Signal(int)
    lost_all_lives  = Signal(Enum)
    sudoku_completed = Signal(Enum) 
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.sudoku = [[" " for _ in range(9)] for _ in range(9)]
        self.statuses = [[[SkColor.WHITE, SkColor.BLACK] for _ in range(9)] for _ in range(9)]  # Grid to store cell statuses
        self.o_sudoku = None
        self.difficulty = None 
        self.wrongs = []
        self.solution = None
        self.lives = 5
        
    def check(self):
        """
        Checks the validity of the Sudoku board.

        Returns:
            bool: True if the board is valid, False otherwise.
        """
        rows = ["".join(row) for row in self.sudoku]
        columns = ["".join(column) for column in zip(*self.sudoku)]
        squares = ["".join(self.sudoku[r][e] for r in range(r1,r1+3) for e in range(e1,e1+3)) for r1 in range(0,9,3) for e1 in range(0,9,3)]
        our_board= [rows,columns,squares]
        for element in our_board:
            for group in element:
                for number in group:
                    if number != " ":
                        if group.count(number) > 1:
                            return False
        return True
    
    def on_life_lost(self):
        self.lives -= 1
        self.lost_one_life.emit(self.lives)

        if self.lives == 0:
            self.lost_all_lives.emit(Game_Statuses.LOST)   
            
    def generate_full_board(self):
        self.sudoku = [[" " for _ in range(9)] for _ in range(9)]
        
        numbers =  [str(i) for i in range(1, 10)]
        shuffle(numbers) 
        self.fill_board(self.sudoku, numbers)

    def fill_board(self, board, numbers):
        empty = self.find_empty(board)
        if not empty:
            return True
        row, col = empty

        for num in numbers:
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                if self.fill_board(board, numbers):
                    return True
                board[row][col] = " "
        return False

    # Solver with backtracking for a given board
    def solve(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True
        row, col = empty

        for num in map(str, range(1, 10)):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                if self.solve(board):
                    return True
                board[row][col] = " "
        return False

    # Check if a number can be placed in a cell
    def is_valid(self, board, num, pos):
        row, col = pos

        # Check row
        if num in board[row]:
            return False
        # Check column
        if num in [board[row][col] for row in range(9)]:
            return False
        # Check box
        box_x, box_y = col // 3, row // 3
        for x in range(box_y * 3, box_y * 3 + 3):
            for y in range(box_x * 3, box_x * 3 + 3):
                if board[x][y] == num:
                    return False
        return True

    # Find an empty space on the board
    def find_empty(self, board):
        for x in range(9):
            for y in range(9):
                if board[x][y] == " ":
                    return (x, y)
        return None

    # Check if the puzzle has a unique solution by trying to solve it twice
    def has_unique_solution(self, board):
        board_copy = deepcopy(board)
        solutions = self.solve_multiple(board_copy, max_solutions=2)
        return solutions == 1

    # A solver that counts solutions up to a certain limit
    def solve_multiple(self, board, max_solutions):
        empty = self.find_empty(board)
        if not empty:
            return 1
        row, col = empty
        solutions = 0

        for num in map(str, range(1, 10)):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                solutions += self.solve_multiple(board, max_solutions)
                board[row][col] = " "
                if solutions >= max_solutions:
                    return solutions
        return solutions
    # Attempts to remove cells until only the desired number of hints remain
   
# Usage
# sudoku = Sudoku()
# sudoku.make_unique_puzzle(hints=25)   # Try to make a puzzle with exactly 17 hints
  
    def generate_sudoku(self, difficulty='Medium', hints=None):
        """
        Set the difficulty of the Sudoku puzzle by removing a certain number of cells.
  
        Args:
            difficulty (str): The difficulty level ('Easy', 'Medium', 'Hard').

        Returns:
            list: A 2D list representing the Sudoku board with empty cells based on difficulty.

        Raises:
            Exception: If an invalid difficulty level is provided.
        """

        if not(hints):
            if difficulty.capitalize() not in ("Easy", "Medium", "Hard", "Test"):
                raise Exception("Invalid difficulty")
            
            dif_index = ("Easy", "Medium", "Hard", "Evil", "Test").index(difficulty)
            
            hints = 39 - 5 * dif_index
            self.lives = 4 + 2 * dif_index
            
            if dif_index == 4:
                hints = 80
                self.lives = 10
            
        else:
            hints = hints
            self.lives = 6

        attempts = 5  
        for attempt in range(attempts):
            self.generate_full_board()
            self.solution = deepcopy(self.sudoku)

            cells = [(x, y) for x in range(9) for y in range(9)]
            shuffle(cells)
            filled_cells = 81

            for row, col in cells:
                if filled_cells <= hints:
                    break
                backup = self.sudoku[row][col]
                self.sudoku[row][col] = " "

                if not self.has_unique_solution(self.sudoku):
                    self.sudoku[row][col] = backup  # Restore if not unique
                else:
                    filled_cells -= 1

            # If we reach the target number of hints, stop
            if filled_cells == hints:
                break
        else:
            print("Could not reach the target hints; generated closest possible.")

        self.statuses = [[[SkColor.WHITE, SkColor.BLACK] for _ in range(9)] for _ in range(9)] 
        
        return self.sudoku

    def set_number(self, x, y, number):
        print(self.sudoku)
        """
        Set a number in the Sudoku board at the given position if the number isn't the correct one.

        Args:
            number (str): The number to set in the board.
            x (int): The row index.
            y (int): The column index.
        """
        if self.sudoku[x][y] != self.solution[x][y]:

            if self.sudoku[x][y] == number:
                self.sudoku[x][y] = " "
                self.statuses[x][y] = [SkColor.WHITE, SkColor.BLACK]
            else: 
                self.sudoku[x][y] = number

    def update_statuses(self, x, y, number):
        """
        Finds coordinates of conflicting numbers on the Sudoku board.

        Args:
            number (str): The number to check.
            x (int): The row index.
            y (int): The column index.
        """
        def convertor(x, y):
            return (x // 3) * 3 + y // 3, (x % 3) * 3 + y % 3

        rows = ["".join(row) for row in self.sudoku]
        columns = ["".join(column) for column in zip(*self.sudoku)]
        squares = ["".join(self.sudoku[r][e] for r in range(r1, r1 + 3) for e in range(e1, e1 + 3)) for r1 in range(0, 9, 3) for e1 in range(0, 9, 3)]
        our_board = [rows, columns, squares]

        wrong_cords = set()
        for group in our_board:
            for x in range(9):
                counter = {}
                safety_pin = True
                for y in range(9):
                    if group == columns:
                        actual_x, actual_y = y, x
                    elif group == squares:
                        actual_x, actual_y = convertor(x, y)
                    else:
                        actual_x, actual_y = x, y

                    if group[x][y] != " ":
                        if group[x][y] not in counter:
                            counter[group[x][y]] = (actual_x, actual_y)
                        else:
                            if safety_pin:
                                wrong_cords.add(counter[group[x][y]])
                                wrong_cords.add((actual_x, actual_y))
                                safety_pin = False
                            else:
                                wrong_cords.add((actual_x, actual_y))
                                
                               
        for x in range(9):
            for y in range(9):
                self.statuses[x][y][0] = SkColor.WHITE      
        # Updates the current grid colors data in logic 
             
        for nums in wrong_cords:
            self.statuses[nums[0]][nums[1]][0] = SkColor.RED
            

    def is_number_valid(self, board, num, pos):
        row, col = pos

        # Check row
        if num in board[row]:
            return False
        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False
        # Check box
        box_x, box_y = col // 3, row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num:
                    return False
        return True

    def is_number_correct(self, x, y, number):
        """
        Check if the number at position (x, y) is the correct number.

        Args:
            x (int): The row index.
            y (int): The column index.
            number (str): The number to check.

        Returns:
            bool: True if the number is correct, False otherwise.
        """
        
        return self.solution[x][y] == number
      

    def check_win(self):
        """
        Checks if the current Sudoku board matches the complete Sudoku solution.

        Returns:
            bool: True if the board matches the solution, False otherwise.
        """
        for x in range(9):
            for y in range(9):
                if self.sudoku[x][y] != self.solution[x][y]:
                    return False
                
        self.sudoku_completed.emit(Game_Statuses.COMPLETED)
        return True

    def print_sudoku(self):
        """Prints the current state of the board"""
        print(f'''
     1   2   3   4   5   6   7   8   9 
   \033[1m+---+---+---+---+---+---+---+---+---+\033[0m
A  \033[1m|\033[0m {self.sudoku[0][0]} | {self.sudoku[0][1]} | {self.sudoku[0][2]} \033[1m|\033[0m {self.sudoku[0][3]} | {self.sudoku[0][4]} | {self.sudoku[0][5]} \033[1m|\033[0m {self.sudoku[0][6]} | {self.sudoku[0][7]} | {self.sudoku[0][8]} \033[1m|\033[0m
   \033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
B  \033[1m|\033[0m {self.sudoku[1][0]} | {self.sudoku[1][1]} | {self.sudoku[1][2]} \033[1m|\033[0m {self.sudoku[1][3]} | {self.sudoku[1][4]} | {self.sudoku[1][5]} \033[1m|\033[0m {self.sudoku[1][6]} | {self.sudoku[1][7]} | {self.sudoku[1][8]} \033[1m|\033[0m
   \033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
C  \033[1m|\033[0m {self.sudoku[2][0]} | {self.sudoku[2][1]} | {self.sudoku[2][2]} \033[1m|\033[0m {self.sudoku[2][3]} | {self.sudoku[2][4]} | {self.sudoku[2][5]} \033[1m|\033[0m {self.sudoku[2][6]} | {self.sudoku[2][7]} | {self.sudoku[2][8]} \033[1m|\033[0m
   \033[1m+---+---+---+---+---+---+---+---+---+\033[0m
D  \033[1m|\033[0m {self.sudoku[3][0]} | {self.sudoku[3][1]} | {self.sudoku[3][2]} \033[1m|\033[0m {self.sudoku[3][3]} | {self.sudoku[3][4]} | {self.sudoku[3][5]} \033[1m|\033[0m {self.sudoku[3][6]} | {self.sudoku[3][7]} | {self.sudoku[3][8]} \033[1m|\033[0m
   \033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
E  \033[1m|\033[0m {self.sudoku[4][0]} | {self.sudoku[4][1]} | {self.sudoku[4][2]} \033[1m|\033[0m {self.sudoku[4][3]} | {self.sudoku[4][4]} | {self.sudoku[4][5]} \033[1m|\033[0m {self.sudoku[4][6]} | {self.sudoku[4][7]} | {self.sudoku[4][8]} \033[1m|\033[0m
   \033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
F  \033[1m|\033[0m {self.sudoku[5][0]} | {self.sudoku[5][1]} | {self.sudoku[5][2]} \033[1m|\033[0m {self.sudoku[5][3]} | {self.sudoku[5][4]} | {self.sudoku[5][5]} \033[1m|\033[0m {self.sudoku[5][6]} | {self.sudoku[5][7]} | {self.sudoku[5][8]} \033[1m|\033[0m
   \033[1m+---+---+---+---+---+---+---+---+---+\033[0m
G  \033[1m|\033[0m {self.sudoku[6][0]} | {self.sudoku[6][1]} | {self.sudoku[6][2]} \033[1m|\033[0m {self.sudoku[6][3]} | {self.sudoku[6][4]} | {self.sudoku[6][5]} \033[1m|\033[0m {self.sudoku[6][6]} | {self.sudoku[6][7]} | {self.sudoku[6][8]} \033[1m|\033[0m
   \033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
H  \033[1m|\033[0m {self.sudoku[7][0]} | {self.sudoku[7][1]} | {self.sudoku[7][2]} \033[1m|\033[0m {self.sudoku[7][3]} | {self.sudoku[7][4]} | {self.sudoku[7][5]} \033[1m|\033[0m {self.sudoku[7][6]} | {self.sudoku[7][7]} | {self.sudoku[7][8]} \033[1m|\033[0m
   \033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
I  \033[1m|\033[0m {self.sudoku[8][0]} | {self.sudoku[8][1]} | {self.sudoku[8][2]} \033[1m|\033[0m {self.sudoku[8][3]} | {self.sudoku[8][4]} | {self.sudoku[8][5]} \033[1m|\033[0m {self.sudoku[8][6]} | {self.sudoku[8][7]} | {self.sudoku[8][8]} \033[1m|\033[0m
   \033[1m+---+---+---+---+---+---+---+---+---+\033[0m ''')
    
        
if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.generate_sudoku(difficulty='Medium')
    sudoku.print_sudoku


