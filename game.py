import random

class XOGame:
    def __init__(self):
        self.reset_board()
        self.current_player = 'X'

    def reset_board(self):
        # 3x3 empty board
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.empty_positions = [(r, c) for r in range(3) for c in range(3)]

    def print_board(self):
        for r in range(3):
            row = " | ".join(self.board[r][c] if self.board[r][c] != "" else " " for c in range(3))
            print(row)
            if r < 2:
                print("---------")

    def get_available_positions(self):
        return self.empty_positions

    def is_valid_move(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
        return self.board[row][col] == ""

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False

        self.board[row][col] = self.current_player
        self.empty_positions.remove((row, col))
        return True

    def make_random_move(self):
        if not self.empty_positions:
            return False

        row, col = random.choice(self.empty_positions)
        self.make_move(row, col)
        return True

    def check_winner(self):
        b = self.board

        # Rows + Columns
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != "":
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != "":
                return b[0][i]

        # Diagonals
        if b[0][0] == b[1][1] == b[2][2] != "":
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != "":
            return b[0][2]

        return None

    def is_board_full(self):
        return len(self.empty_positions) == 0

    def is_game_over(self):
        if self.check_winner() is not None:
            return True
        if self.is_board_full():
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        self.reset_board()
        self.current_player = 'X'

        while not self.is_game_over():
            self.make_random_move()
            self.board
            if not self.is_game_over():
                self.switch_player()

        return self.check_winner()
