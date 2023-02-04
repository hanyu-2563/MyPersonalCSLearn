BOARD_SIZE=15
def print_board(board):
    for i in range(BOARD_SIZE):
        print("+---" * BOARD_SIZE + "+")
        row = "|"
        for j in range(BOARD_SIZE):
            if board[i][j] == "X":
                row += " X |"
            elif board[i][j] == "O":
                row += " O |"
            else:
                row += "   |"
        print(row)
    print("+---" * BOARD_SIZE + "+")

# 状态判断
GAMEOVER_WIN=1
GMAEOVER_TIE=2
GAME_OVER_CONTINUE = 3
def init_board():
    
