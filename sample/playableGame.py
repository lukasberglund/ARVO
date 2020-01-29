import sample.board as board
board = board.Board()

def get_next_sub_board():
    if board.next_move == (-1,-1):
        #get user entered subX,subY
        print("You can choose which sub_board you want to play in next.")
        nextSub = input("Enter the row and column separated by a comma : ")
        nextSub = nextSub.split(',')
        (subX,subY) = tuple((int(str) for str in nextSub))
        #check that subX and subY are valid
        while not board.is_valid(subX,subY):
            nextSub = input("Please enter a valid row and column separated by a comma : ")
            nextSub = nextSub.split(',')
            (subX,subY) = tuple((int(str) for str in nextSub))
    else:
        (subX, subY) = board.next_move
        print("You must play in sub_board ", subX, ",",subY)

    return (subX,subY)

def get_next_move(subX,subY):

    nextMove = input("Choose your move. Enter the row and column separated by a comma: ")
    nextMove = nextMove.split(',')
    (x,y) = tuple((int(str) for str in nextMove))

    #check that desired move is open
    while not board.is_open(subX,subY,x,y):
        nextMove = input("Choose an open move. Enter the row and column separated by a comma: ")
        nextMove = nextMove.split(',')
        (x,y) = tuple((int(str) for str in nextMove))

    return (x,y)


print("Please note that all board positions are w.r.t row and column starting from 0")
print("Enjoy the game")

while (not board.is_won and not board.num_boxes == 9):

    print("Turn: Player", board.turn + 1)
    print("The board looks like this: " )
    print(board)

    (subX,subY) = get_next_sub_board()

    (x,y) = get_next_move(subX,subY)

    board.play_move(subX,subY,x,y) #do move and update board

print("The game is over.", "Player", board.turn + 1, "has won.", "Here is the final board")
