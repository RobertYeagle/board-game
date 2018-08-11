from random import choice

def initializegrid(board):
    # initialize grid by random value
    for i in range(8):
        for j in range (8):
            board[i][j] = choice(['Q','R','S','T','U'])


def initialize(board):
    # intialize the game
    # initialize gird
    initializegrid(board)
    # intialize score
    global score
    score = 0
    # initialize turn number
    global turn
    turn = 1


def continuegame(current_score, goalscore = 100):
    # retun false if the game should end, true if the game is not over
    if (current_score >= goalscore):
        return False
    else:
        return True
    # print ("Checking to see if we should continue")

def drawboard(board):
    linetodraw=""
    print ("\n\n\n")
    print (" ---------------------------------")
    for i in range(7,-1,-1):
        linetodraw = ""
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw+= " |"
        print(linetodraw)
        print(" ---------------------------------")


def getmove():
    # get the move from the user
    move = input("Enter move: ")
    return move

def update(board,move):
    # update the board according to move
    print("Updating board")

def doround(board):
    # perform one round of the game
    # display current board
    drawboard(board)
    # get move
    move = getmove()
    #update board
    update(board, move)
    #update tunr number
    global turn
    turn += 1

def convertlettertocol(col):
    if col == 'a':
        return 0
    elif col == 'b':
        return 1
    elif col == 'c':
        return 2
    elif col == 'd':
        return 3
    elif col == 'e':
        return 4
    elif col == 'f':
        return 5
    elif col == 'g':
        return 6
    elif col == 'h':
        return 7
    else:
        # not a valid column
        return -1

def swappieces(board, move):
    # swap pieces on board according to move
    origrow = int(move[1])-1
    origcol = convertlettertocol(move[0])

    if move[2] == 'u':
        newrow = origrow + 1
        newcol = origcol
    elif move[2] == 'd':
        newrow = origrow - 1
        newcol = origcol
    elif move[2] == 'l':
        newrow = origrow
        newcol = origcol - 1
    elif move[2] == 'r':
        newrow = origrow
        newcol = origcol + 1

    temp = board[origrow][origcol]
    board[origrow][origcol] = board[newrow][newcol]
    board[newrow][newcol] = temp


def removepieces(board):
    # remove 3 in a row nd 3 ina  column pieces
    # create board ot store remove or not
    remove = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(8):
        for j in range(6):
            if (board[i][j] == board[i][j+1]) and (board[i][j] == board[i][j+2]):
                # three in a row are the same!
                remove[i][j]= 1;
                remove[i][j+1] = 1;
                remove[i][j+2] = 1;

    for i in range(8):
        for j in range(6):
            if (board[i][j] == board[i+1][j]) and (board[i][j] == board [i+2][j]):
                # three in a row are the same!
                remove[i][j]= 1;c3
                remove[i+1][j] = 1;
                remove[i+2][j] = 1;

    # elimate those marked
    global score
    removed_any = False
    for i in range (8):
        for j in range(8):
            if remove[i][j] == 1:
                board[i][j] = 0
                score += 1
                removed_any = True
    return removed_any


def droppieces(board):
    # drop pieces to fill in blanks
    for j in range(8):
        # make list of pieces in the column
        listofpieces = []
        for i in range(8):
            if board[i][j] != 0:
                listofpieces.append(board[i][j])
            # copy that list into a column
            for i in range(len(listofpieces)) :
                board[i][j] = listofpieces[i]
            # fill in the reminders with 0
            for i in range(len(listofpieces),8):
                board[i][j] = 0


def fillblanks(board):
    for i in range(8):
        for j in range(8):
            if (board[i][j] == 0):
                board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])


def update(board, move):
    swappieces(board, move)
    pieces_eliminated = True
    while pieces_eliminated:
        pieces_eliminated = removepieces(board)
        droppieces(board)
        fillblanks(board)





# state main variables
score = 100
turn = 100
goalscore = 100
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]


# initialize the game
initialize(board)

# loop while game not over
while continuegame(score, goalscore):
    # do round of the game
    doround(board)