


board = Board()

while (not board.is_won and not board.num_moves == 9):

    # Ask current player for move (board.turn) and (board.next_move)
    #get next move in x,y format
    #check board.next_move is valid on board

    if board.next_move == (-1,-1):
        #get user entered subX,subY
        #check that subX and subY are valid
    else:
        (subX, subY) = board.next_move
    #get user entered x,y
    #check that desired move is open
    if board.is_open(subX,subY,x,y):
        board.play_move(subX,subY,x,y) #do move and update board

    # Print board
