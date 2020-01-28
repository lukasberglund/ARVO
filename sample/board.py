class Board:
    def __init__(self):
        self.turn = 0
        self.sub_boards = self.gen_sub_boards()
        self.is_won = False
        self.winner = ""
        self.num_boxes = 0
        self.next_move = (-1,-1)

    def gen_sub_boards(self):
        sub_boards = []
        for row in range(3):
            sub_boards.append([])
            for col in range(3):
                sub_boards[row].append(SubBoard())
        return sub_boards

    def __repr__(self):
        big_rows = [] #contains rows of sub_boards
        for big_row in range(3):
            big_rows.append(self.big_row_as_str(big_row))
        return "\n" + "\n\n\n".join(big_rows) + "\n"

    def big_row_as_str(self, row):
        """Represents the n_th row of sub_boards as a string """
        line_seperator = "\n-----------     -----------     -----------\n"
        sub_rows = []
        for sub_row in range(3):
            sub_rows.append(self.sub_row_as_str(row, sub_row))
        return line_seperator.join(sub_rows)

    def sub_row_as_str(self, row, sub_row):
        """Represents small rows as strings"""
        cols = []
        for col in range(3):
            cols.append(self.sub_boards[row][col].row_as_str(sub_row))
        return "     ".join(cols)



    def is_valid(self,x,y):
        return (not self.sub_boards[x][y].is_won and not self.sub_boards[x][y].num_moves == 9
        and x < 3 and x >= 0 and y < 3 and y >= 0)

    def is_open(self,x1,y1,x2,y2):
        return self.sub_boards[x1][y1].is_open(x2,y2)

    #plays moves at sub_board x1,y1 and position x2,y2 and updates turn,won,num_moves
    def play_move(self,x1,y1,x2,y2):
        self.sub_boards[x1][y1].play_move(x2,y2,self.turn)
        self.turn = (self.turn + 1) % 2
        #update sub_board if won
        if self.sub_boards[x1][y1].is_won or self.sub_boards[x1][y1].num_moves == 9:
            self.num_boxes += 1
        #update next_move
        self.next_move = (x2,y2)
        if self.sub_boards[x2][y2].is_won or self.sub_boards[x2][y2].num_moves == 9 :
            self.next_move = (-1,-1)

    def check_won(self,piece): #check if won and update winner and is_won if necessary
        #brute force
        return self.col_won(piece) or self.row_won(piece) or self.diagon_won(piece)

    def col_won(self,piece):
        won = False
        col = 0
        while not won or col < 3:
            won = (self.sub_boards[0][col] == piece and self.sub_boards[1][col] == piece and self.sub_boards[2][col] == piece)
            col += 1

        return won

    def row_won(self,piece):
        won = False
        row = 0
        while not won or row < 3:
            won = (self.sub_boards[row][0] == piece and self.sub_boards[row][1] == piece and self.sub_boards[row][2] == piece)
            row += 1
        return won

    def diagon_won(self,piece):
        if self.sub_boards[0][0] == piece and self.sub_boards[1][1] == piece and self.sub_boards[2][2] == piece:
            return True
        if self.sub_boards[0][2] == piece and self.sub_boards[1][1] == piece and self.sub_boards[2][0] == piece:
            return True
        return False

class SubBoard:
    def __init__(self):
        self.is_won = False
        self.winner = ""
        self.fields = self.gen_fields()
        self.num_moves = 0

    def gen_fields(self):
        fields = []
        for col in range(3):
            fields.append([])
            for row in range(3):
                fields[col].append(" ")
        return fields

    def get_field(self, row, col):
        return self.fields[row][col]

    def row_as_str(self, row):
        return " " + ' | '.join(self.fields[row]) + " "

    def is_full(self):
        return self.is_won or self.moves == 9

    def is_open(self,x,y):
        return x >= 0 and x < 3 and y >= 0 and y < 3 and self.fields[x][y] == " "

    #update (x,y) on field to have the player's sign
    #update num_moves,winner, is_won, etc.
    def play_move(self,x,y,player):
        if player == 0:
            piece = "X"
        else:
            piece = "O"

        self.fields[x][y] = piece
        self.num_moves += 1
        if self.check_won(piece):
            self.is_won = True
            self.winner = piece

    def check_won(self,piece): #check if won and update winner and is_won if necessary
        #brute force
        return self.col_won(piece) or self.row_won(piece) or self.diagon_won(piece)

    def col_won(self,piece):
        won = False
        col = 0
        while not won and col < 3:
            won = self.fields[0][col] == piece and self.fields[1][col] == piece and self.fields[2][col] == piece
            col = col + 1
        return won

    def row_won(self,piece):
        won = False
        row = 0
        while not won and row < 3:
            return self.fields[row][0] == piece and self.fields[row][1] == piece and self.fields[row][2] == piece
            row = row + 1
        return won

    def diagon_won(self,piece):
        if self.fields[0][0] == piece and self.fields[1][1] == piece and self.fields[2][2] == piece:
            return True
        if self.fields[0][2] == piece and self.fields[1][1] == piece and self.fields[2][0] == piece:
            return True
        return False
