from game import XOGame

def test_empty_board():
    game = XOGame()
    assert len(game.get_available_positions()) == 9

def test_valid_move():
    game = XOGame()
    assert game.make_move(1, 1) == True

def test_invalid_move():
    game = XOGame()
    game.make_move(0, 0)
    assert game.make_move(0, 0) == False 

def test_row_win():
    game = XOGame()
    game.make_move(0, 0)
    game.make_move(0, 1)
    game.make_move(0, 2)
    assert game.check_winner() == 'X'

def test_col_win():
    game = XOGame()
    game.make_move(0, 1)
    game.make_move(1, 1)
    game.make_move(2, 1)
    assert game.check_winner() == 'X'

def test_diag_win():
    game = XOGame()
    game.make_move(0, 0)
    game.make_move(1, 1)
    game.make_move(2, 2)
    assert game.check_winner() == 'X'

def test_tie():
    game = XOGame()
    moves = [
        ('X', 0, 0), ('O', 0, 1), ('X', 0, 2),
        ('X', 1, 0), ('O', 1, 1), ('X', 1, 2),
        ('O', 2, 0), ('X', 2, 1), ('O', 2, 2)
    ]
    for sym, r, c in moves:
        game.board[r][c] = sym
        if (r, c) in game.empty_positions:
            game.empty_positions.remove((r, c))

    assert game.check_winner() is None
    assert game.is_board_full() == True

def test_multiple_games():
    results = {'X': 0, 'O': 0, 'tie': 0}

    for i in range(100):
        game = XOGame()
        winner = game.play_game()
        if winner:
            results[winner] += 1
        else:
            results['tie'] += 1

    print(results)
    assert sum(results.values()) == 100

