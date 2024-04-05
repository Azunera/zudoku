from random import randrange, shuffle, choice
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


#Temporal display on terminal
def boarddisplay():
    print(f'''
\033[1m+---+---+---+---+---+---+---+---+---+\033[0m
\033[1m|\033[0m {board[0][0]} | {board[0][1]} | {board[0][2]} \033[1m|\033[0m {board[0][3]} | {board[0][4]} | {board[0][5]} \033[1m|\033[0m {board[0][6]} | {board[0][7]} | {board[0][8]} \033[1m|\033[0m
\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
\033[1m|\033[0m {board[1][0]} | {board[1][1]} | {board[1][2]} \033[1m|\033[0m {board[1][3]} | {board[1][4]} | {board[1][5]} \033[1m|\033[0m {board[1][6]} | {board[1][7]} | {board[1][8]} \033[1m|\033[0m
\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
\033[1m|\033[0m {board[2][0]} | {board[2][1]} | {board[2][2]} \033[1m|\033[0m {board[2][3]} | {board[2][4]} | {board[2][5]} \033[1m|\033[0m {board[2][6]} | {board[2][7]} | {board[2][8]} \033[1m|\033[0m
\033[1m+---+---+---+---+---+---+---+---+---+\033[0m
\033[1m|\033[0m {board[3][0]} | {board[3][1]} | {board[3][2]} \033[1m|\033[0m {board[3][3]} | {board[3][4]} | {board[3][5]} \033[1m|\033[0m {board[3][6]} | {board[3][7]} | {board[3][8]} \033[1m|\033[0m
\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
\033[1m|\033[0m {board[4][0]} | {board[4][1]} | {board[4][2]} \033[1m|\033[0m {board[4][3]} | {board[4][4]} | {board[4][5]} \033[1m|\033[0m {board[4][6]} | {board[4][7]} | {board[4][8]} \033[1m|\033[0m
\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
\033[1m|\033[0m {board[5][0]} | {board[5][1]} | {board[5][2]} \033[1m|\033[0m {board[5][3]} | {board[5][4]} | {board[5][5]} \033[1m|\033[0m {board[5][6]} | {board[5][7]} | {board[5][8]} \033[1m|\033[0m
\033[1m+---+---+---+---+---+---+---+---+---+\033[0m
\033[1m|\033[0m {board[6][0]} | {board[6][1]} | {board[6][2]} \033[1m|\033[0m {board[6][3]} | {board[6][4]} | {board[6][5]} \033[1m|\033[0m {board[6][6]} | {board[6][7]} | {board[6][8]} \033[1m|\033[0m
\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
\033[1m|\033[0m {board[7][0]} | {board[7][1]} | {board[7][2]} \033[1m|\033[0m {board[7][3]} | {board[7][4]} | {board[7][5]} \033[1m|\033[0m {board[7][6]} | {board[7][7]} | {board[7][8]} \033[1m|\033[0m
\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---\033[1m+\033[0m---+---+---+\033[0m
\033[1m|\033[0m {board[8][0]} | {board[8][1]} | {board[8][2]} \033[1m|\033[0m {board[8][3]} | {board[8][4]} | {board[8][5]} \033[1m|\033[0m {board[8][6]} | {board[8][7]} | {board[8][8]} \033[1m|\033[0m
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
    global board
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
                        # print(e, "E", t, "TURN")
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
                
            
