class Board:
    def __init__(self):
        self.turn = 1
        self.sub_boards = self.gen_sub_boards()
        self.is_won = False
        self.winner = ""

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

class SubBoard:
    def __init__(self):
        self.is_won = False
        self.winner = ""
        self.fields = self.gen_fields()

    def gen_fields(self):
        fields = []
        for col in range(3):
            fields.append([])
            for row in range(3):
                fields[col].append(" ")
        return fields

    def get_field(row, col):
        return self.fields[row][col]

    def row_as_str(self, row):
        return " " + ' | '.join(self.fields[row]) + " "
