import copy
def display_board (board) :
    print ('+' + '-'*7 + '+' + '-'*7 + '+' + '-'*7 + '+')
    print ('|' ,'|' ,'|', '|', sep=' '*7)
    print ('|' ,' ', board [0][0],' ' ,'|', end = '')
    print (' '*2, board [0][1],' ' ,'|', end = '')
    print (' '*2, board [0][2],' ' ,'|')
    print ('|' ,'|' ,'|', '|', sep=' '*7)
    print ('+' + '-'*7 + '+' + '-'*7 + '+' + '-'*7 + '+')
    print ('|' ,'|' ,'|', '|', sep=' '*7)
    print ('|' ,' ', board [1][0],' ' ,'|', end = '')
    print (' '*2, board [1][1],' ' ,'|', end = '')
    print (' '*2, board [1][2],' ' ,'|')
    print ('|' ,'|' ,'|', '|', sep=' '*7)
    print ('+' + '-'*7 + '+' + '-'*7 + '+' + '-'*7 + '+')
    print ('|' ,'|' ,'|', '|', sep=' '*7)
    print ('|' ,' ', board [2][0],' ' ,'|', end = '')
    print (' '*2, board [2][1],' ' ,'|', end = '')
    print (' '*2, board [2][2],' ' ,'|')
    print ('|' ,'|' ,'|', '|', sep=' '*7)
    print ('+' + '-'*7 + '+' + '-'*7 + '+' + '-'*7 + '+')

def enter_move (board) :
    move = int(input ("Enter your move: "))
    free = make_list_of_free_fields(board)
    if move not in range (1,10) :
        print ("refused... Enter your move: ")
    for row in range (3) :
        for col in range (3) :
            spot_tup = (row,col)
            if move == board[row][col] :
                if spot_tup not in free :
                    print("Move already taken")
                else :
                    board [row][col]= "O"

def make_list_of_free_fields(board) :
    free = []
    for row in range (3):
        for col in range (3):
            if board [row][col] == "X" or board [row][col] == "O" :
                continue
            free.append((row,col))
    return free
    
def victory_for (board,sign) :
    for row in range (3) :
        if board[row][0] == board[row][1] == board[row][2] == sign :
            return True

    for col in range (3) :
        if board[0][col] == board[1][col] == board[2][col] == sign :
            return True

    if board[0][0] == board [1][1] == board [2][2] == sign or \
    board[0][2]==board[1][1]==board[2][0]==sign :
        return True

def draw_move(board) :
    from random import randrange
    free_fields = make_list_of_free_fields(board)
    row = randrange(3)
    col = randrange(3)
    while (row,col) not in free_fields :
        row = randrange(3)
        col = randrange(3)
    board[row][col] = "X"
    return board

def fun_rev_board (coded_board) :
    rev_board = copy.deepcopy(coded_board)
    for row in range (3) :
        for col in range (3) :
            rev_board[row][col]= board[col][row]
    return rev_board


def code_the_board (board):
    coded_board = copy.deepcopy(board) 
    for row in range (3):
        for col in range (3):
            if type(board[row][col]) == int :
                coded_board[row][col] = None
            elif  board[row][col] == "X" :
                coded_board[row][col] = 1
            elif board [row][col] == "O" :
                coded_board[row][col] = 0
    return coded_board



def next_move (board):
    coded_board = code_the_board(board) 
    rev_board = fun_rev_board (coded_board)
    first_diagonal = [coded_board[0][0], coded_board[1][1], coded_board[2][2]]
    second_diagonal =[coded_board[0][2], coded_board[1][1], coded_board[2][0]]
    num_X1 = first_diagonal.count(1)
    num_X2 = second_diagonal.count(1)
    num_O1 = first_diagonal.count(0)
    num_O2 = second_diagonal.count(0)

    #check X's
       #checking rows
    for row in range (3) :
         num_X = coded_board[row].count(1)
         if num_X == 2 and None in coded_board[row]:
             target = coded_board[row].index(None)
             board[row][target]="X"
             return
        #checking cols
    for row in range (3) :
         num_X = rev_board[row].count(1)
         if num_X == 2 and None in rev_board[row]:
             target = coded_board[row].index(None)
             board[target][row]="X"
             return
        #checking diagonals
    if num_X1 == 2 and None in first_diagonal :
        target_diag = first_diagonal.index(None)
        if target_diag == 0:
            board[0][0] = "X"
            coded_board[0][0] = 1
        elif target_diag == 1:
            board[1][1] = "X"
            coded_board[1][1] = 1
        elif target_diag == 2:
            board[2][2] = "X"
            coded_board[2][2] = 1
        return
    if num_X2 == 2 and None in second_diagonal :
        target_diag = second_diagonal.index(None)
        if target_diag == 0:
            board[0][2] = "X"
            coded_board[0][2] = 1
        elif target_diag == 1:
            board[1][1] = "X"
            coded_board[1][1] = 1
        elif target_diag == 2:
            board[2][0] = "X"
            coded_board[2][0] = 1
        return
    #check O's
       #checking rows
    for row in range(3) :
         num_O = coded_board[row].count(0)
         if num_O == 2 and None in coded_board[row] :
             target = coded_board[row].index(None)
             board[row][target]="X"
             return
       #checking cols
    for row in range (3) :
         num_O = rev_board[row].count(0)
         if num_O == 2 and None in rev_board[row] :
             target = coded_board[row].index(None)
             board[target][row]="X"
             return
        #checking diagonals
    if num_O1 == 2 and None in first_diagonal :
            target_diag = first_diagonal.index(None)
            if target_diag == 0:
                board[0][0] = "X"
                coded_board[0][0] = 1
            elif target_diag == 1:
                board[1][1] = "X"
                coded_board[1][1] = 1
            elif target_diag == 2:
                board[2][2] = "X"
                coded_board[2][2] = 1
            return
    if num_O2 == 2 and None in second_diagonal :
            target_diag = second_diagonal.index(None)
            if target_diag == 0:
                board[0][2] = "X"
            elif target_diag == 1:
                board[1][1] = "X"
            elif target_diag == 2:
                board[2][0] = "X"
            return
    draw_move(board)

def tie_detector(board):
    for row in board :
        for elem in row :
            if type(elem) == int :
                return False
    print("Tie") 
    return True   




board = [[1,2,3],[4,5,6],[7,8,9]]
display_board(board)
while True :
    enter_move(board) 
    display_board(board)
    if victory_for (board,"X") :
        print("Player X has won!")
        break
    elif victory_for (board,"O") :
        print("Player O has won!")
        break
    elif tie_detector(board) :
        print ("It's a tie !!")
        break
    next_move(board)
    display_board(board)
    if victory_for (board,"X") :
        print("Player X has won!")
        break
    elif victory_for (board,"O") :
        print("Player O has won!")
        break
    elif tie_detector(board) :
        print ("It's a tie !!")
    
print ("Thank you!!")


