from random import randrange, shuffle, choice, sample
from time import sleep

board = [[" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "]]

def boarddisplay():
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

def check(boardd):
    
    rows = ["".join(row) for row in boardd]
    columns = ["".join(column) for column in zip(*boardd)]
    squares = ["".join(boardd[r][e] for r in range(r1,r1+3) for e in range(e1,e1+3)) for r1 in range(0,9,3) for e1 in range(0,9,3)]
    our_board= [rows,columns,squares]
    for element in our_board:
        for group in element:
            for number in group:
                if number != " ":
                    if group.count(number) > 1:
                        return False
    return True

def randomgenerator():
    board = [[" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "]]
    hisd= ""
    n= 1
    r= -1
    t=1
    history=[]
    blacklist={}
    while n<10:
        r += 1
        if r >8:
            n += 1
            r = 0
        ii = True
        g = True
        if n==10: break
    
        while g:
            # print("Current state of the board:")
            # boarddisplay()
            # print("Trying to fill number", n, "at row", r)
            indexes= "012345678"
            try:
                for el in blacklist[str(t)]:
                    for e in el:

                        indexes= indexes.replace(e,"")
            except:
                    pass
                    
            indexes= [int(e) for e in indexes]
            shuffle(indexes)
            for i in indexes:
                if board[r][i] == " ":
                    board[r][i] = str(n)
                    # print("Attempting to fill cell (", r, ",", i, ") with number", n)
                    if check(board):
                        # print("Valid configuration so far:")
                        # boarddisplay()
                        g = False
                        ii = False
                        break
                    else:
                        # print("Invalid configuration. Clearing cell (", r, ",", i, ")")
                        board[r][i] = " "

            if ii:
                # retracing, 
                try:
                    del blacklist[str(t)]
                except:
                    pass
                t-= 1
                hisd= history[-1][2]
                board[int(history[-1][0])][int(hisd)] = " "
                try:
                    if hisd not in blacklist[str(t)]:
                        blacklist[str(t)] += (hisd,)
                except:
                    blacklist[str(t)] = (hisd,)                   
                del history[-1]
            
                r -= 1
                if r < 0:
                    r = 8
                    n -= 1
                
            else:
                history.append(f'{r}:{i}:{t}')
                t+=1     
    return board

def difficulty(board, dif):
    if dif.capitalize() not in ("Easy", "Medium", "Hard"):
        raise Exception("Invalid difficulty")

    if dif == 'Easy':
        empty_cells = 40
    elif dif == 'Medium':
        empty_cells = 50
    else:  # 'Hard'
        empty_cells = 60
        

    for __ in range(empty_cells):
        row, col = sample(range(9), 2)
        while board[row][col] == " ":
            row, col = sample(range(9), 2)
        board[row][col] = " "
        
    return board

def picking():
    global board
    global lives

    loc = input("Choose a cell (in a pattern like C3, H1): ")

    def cordchecker(loc):
        global board
        while True:
            
            if loc[0] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'] or loc[1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or len(loc) != 2:
                loc = input("Please insert a valid pattern (C3, H1): ")
                continue
            x = ord(loc[0].upper()) - ord('A')
            y = int(loc[1]) - 1
            print(x,y)
            boarddisplay()
            if board[x][y] == " ":
                return x, y
            else:
                loc = input("Please choose an empty cell: ")

    def numberchoosing(x, y):
        global board
        number = input("Please insert a number to put in cell (to change cell, insert new coord): ")
        if len(number) == 1 and number.isdigit():
            board[x][y] = number
        elif number[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'] and number[1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and len(number) == 2:
            x,y = cordchecker(number)
            numberchoosing(x,y)
        # else:
        #     print("Invalid input! You must enter a single-digit number.")


    def checker(x,y):
        print("im here!")
        
        global board
        global lives
        while not check(board):
            print("Wrong number! You lost a life. You have", lives, "lives left.")
            board[x][y] = " "
            lives -= 1
            if lives == 0:
                print("Game over!")
                return False
            loc = input("Please insert a new number or change coord: ")
            x, y = cordchecker(loc)
            print(x,y, 'IN checker')
            numberchoosing(x, y)

    x, y = cordchecker(loc)
    
    numberchoosing(x, y)
    checker(x,y)
   
def winner_check():
    global board
    for row in range(9):
        for number in range(9):
            if board[row][number] == " ":
                return True
    return False
    
def try_again():
    global board
    board = [[" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "]]
    sudoku()
    

if __name__ == "__main__":          
    def sudoku():
        global lives
        print("Welcome to Sudoku!")
        lives = 5
        sleep(1)
        randomgenerator()
        difficulty()
        boarddisplay()
        while winner_check() and lives != 0:
            picking()
            boarddisplay()
            
        if lives == 0:
            print("Game over!, Good try!")
            try_again()
        else:
            print("Congrats!, you won!")
            try_again()
    sudoku()
            
        
