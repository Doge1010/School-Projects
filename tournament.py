import csv
import os
import time
from datetime import datetime
from game import XOGame


class XOTournament:
    def __init__(self, num_games=100, csv_filename="tournament_results.csv"):
        self.num_games = num_games
        self.csv_filename = csv_filename

        self.reset_tournament()

    def reset_tournament(self):
        self.results = []  
        self.x_wins = 0
        self.o_wins = 0
        self.ties = 0

    def run_tournament(self):
        print(f"Starting tournament of {self.num_games} games...")

        for game_number in range(1, self.num_games + 1):
            self.run_single_game(game_number)

            if game_number % 50 == 0:
                self.save_results_to_csv(self.csv_filename)

        self.save_results_to_csv(self.csv_filename)

        print("Tournament finished ✅")

    def run_single_game(self, game_number):
        game = XOGame()

        start_time = time.perf_counter()
        winner = game.play_game()
        duration = (time.perf_counter() - start_time) * 1000  # ms

        moves_count = 9 - len(game.empty_positions)

        final_board = ";".join([
            "".join(cell if cell != "" else " " for cell in row)
            for row in game.board
        ])

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if winner == 'X':
            self.x_wins += 1
        elif winner == 'O':
            self.o_wins += 1
        else:
            winner = "Tie"
            self.ties += 1

        self.record_game_result(
            game_number,
            winner,
            moves_count,
            duration,
            final_board,
            timestamp
        )

    def record_game_result(self, game_number, winner, moves, duration, board_state, timestamp):
        self.results.append({
            "game_number": game_number,
            "winner": winner,
            "moves_count": moves,
            "duration": duration,
            "final_board": board_state,
            "timestamp": timestamp
        })

    def save_results_to_csv(self, filename):

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                "Game_Number", "Winner", "Moves_Count",
                "Duration_MS", "Final_Board", "Timestamp"
            ])

            for r in self.results:
                writer.writerow([
                    r["game_number"],
                    r["winner"],
                    r["moves_count"],
                    round(r["duration"], 3),
                    r["final_board"],
                    r["timestamp"]
                ])

    def load_results_from_csv(self, filename):
        if not os.path.exists(filename):
            print("File not found.")
            return False

        self.reset_tournament()
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.results.append(row)

                if row["Winner"] == "X":
                    self.x_wins += 1
                elif row["Winner"] == "O":
                    self.o_wins += 1
                else:
                    self.ties += 1

        return True

    def get_win_percentage(self, player):
        total = len(self.results)
        if total == 0:
            return 0.0

        if player == 'X':
            return (self.x_wins / total) * 100
        if player == 'O':
            return (self.o_wins / total) * 100

        return 0.0

    def get_average_game_length(self):
        if not self.results:
            return 0
        return sum(int(r["moves_count"]) for r in self.results) / len(self.results)

    def print_basic_stats(self):
        total = len(self.results)
        print("=== Basic Stats ===")
        print(f"Total games: {total}")
        print(f"X wins: {self.x_wins} ({self.get_win_percentage('X'):.1f}%)")
        print(f"O wins: {self.o_wins} ({self.get_win_percentage('O'):.1f}%)")
        print(f"Ties: {self.ties}")

    def print_detailed_stats(self):
        self.print_basic_stats()

        print("\n=== Advanced Stats ===")
        print(f"Average moves per game: {self.get_average_game_length():.2f}")

tour = XOTournament()
tour.run_tournament()