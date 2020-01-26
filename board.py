class Board:
    def __init__(self):
        self.turn = 1
        self.sub_boards = self.gen_sub_boards()
        self.is_won = False
        self.winner = ""

    def gen_sub_boards(self):
        sub_boards = []
        for col in range(3):
            self.sub_boards.append([])
            for row in range(3):
                self.sub_boards[col].append(SubBoard())
        return sub_boards

class SubBoard:
    def __init__(self):
        self.is_won = False
        self.winner = ""
        self.fields = self.gen_fields

    def gen_fields(self):
        fields = []
        for col in range(3):
            self.fields.append([])
            for row in range(3):
                self.fields[col].append(" ")
        return sub_boards
