import random 

class XOGame:
    def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.current_player = "X"

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = " "
    
    def print_board(self):
        for row in range(3):
            for col in range(3):
                print((str(self.board[row][col])), end=", ")
            print()
    
    def get_available_positions(self):
        available_positions = []
        for row in range(3):
            for col in range(3):
                if(self.board[row][col] == " "):
                    available_positions.append((row, col))
        return available_positions
    
    def switch_player(self):
        if(self.current_player == "X"):
            self.current_player = "O"
        else:
            self.current_player = "X"

    def is_valid_move(self, row, col):
        return self.board[row][col] == " "
    
    def make_move(self, row, col):
        if(self.is_valid_move(row, col)):
            self.board[row][col] = self.current_player
            self.switch_player()
        else:
            return "Move not made"

    def make_random_move(self):
        row, col = random.choice(self.get_available_positions())
        self.board[row][col] = self.current_player
        self.switch_player()
    
    def check_winner(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        if self.board[0][0] == self.board[1][0] == self.board[2][0]:
            return self.board[0][0]
        if self.board[0][1] == self.board[1][1] == self.board[2][1]:
            return self.board[0][1]
        if self.board[0][2] == self.board[1][2] == self.board[2][2]:
            return self.board[0][2]
        if self.board[0][0] == self.board[0][1] == self.board[0][2]:
            return self.board[0][0]
        if self.board[1][0] == self.board[1][1] == self.board[1][2]:
            return self.board[1][0]
        if self.board[2][0] == self.board[2][1] == self.board[2][2]:
            return self.board[2][0]
        return None

    
    def is_board_full(self):
        return self.get_available_positions() == None

    def is_game_over(self):
        winner = self.check_winner()
        if(self.is_board_full()):
            winner = self.check_winner()
            if(winner == None):
                return "Tie"
        if(winner != None):
            return winner

def main():
    game = XOGame()
    for i in range(9):
        game.make_random_move()
    game.print_board()
    print()
    print("winner:", game.is_game_over())

main()
