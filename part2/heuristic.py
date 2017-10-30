import random

def offensive_heuristic(player, chessboard):
    remaining_pieces = 0
    opponent = ""
    if (player == "B"):
        opponent = "W"
    else:
        opponent = "B"
    for i in range(8):
        for j in range(8):
            if (chessboard[i][j] == opponent):
                remaining_pieces += 1
    return 2*(30 - remaining_pieces) + random.random()


def defensive_heuristic(player, chessboard):
    remaining_pieces = 0
    for i in range(8):
        for j in range(8):
            if (chessboard[i][j] == player):
                remaining_pieces += 1
    return 2*(remaining_pieces) + random.random()
