from sample import board

empty_board = board.Board()
empty_sub_board = empty_board.sub_boards[0][0]


class TestClass:
    def test_is_won_field(self):
        assert empty_board.is_won == False
    def test_turn_field(self):
        assert empty_board.turn == 1
    def test_winner_field(self):
        assert empty_board.winner == ""
    def test_sub_boards_field(self):
        assert len(empty_board.sub_boards) == 3
        assert len(empty_board.sub_boards[0]) == 3
    def test_sub_boards_is_won_field(self):
        assert empty_sub_board.is_won == False
    def test_sub_board_is_winner_field(self):
        assert empty_sub_board.winner == ""
    def test_sub_board_get_field(self):
        assert empty_sub_board.get_field(2, 2) == " "
