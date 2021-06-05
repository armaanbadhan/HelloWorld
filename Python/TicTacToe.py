
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]


def CheckVictory(bo, a, b):

    # check if previous move caused a win on vertical line 
    if bo[0][b] == bo[1][b] == bo[2][b]:
        return True

    # check if previous move caused a win on horizontal line 
    if bo[a][0] == bo[a][1] == bo[a][2]:
        return True

    # check if previous move was on the main diagonal and caused a win
    if a == b and bo[0][0] == bo[1][1] == bo[2][2]:
        return True

    # check if previous move was on the secondary diagonal and caused a win
    if a + b == 2 and bo[0][2] == bo[1][1] == bo[2][0]:
        return True

    return False


def play(p):
    global x, y, draw
    try:
        x, y = map(int, input("Player {}\nWhere do you want to mark: ".format(p)).strip().split())
    except ValueError:
        print("Enter a valid position")
        play(p)

    if p == 1:
        draw = "X"
    elif p == 2:
        draw =  "O"

    try:
        if board[x][y] == "-":
            board[x][y] = "{}".format(draw)
        else:
            print("Already occupied")
            play(p)
    except IndexError:
        print("Enter a valid position")
        play(p)
    print('\n'.join([str(lst) for lst in board]))

    if CheckVictory(board, x, y):
        print("Player {} WON".format(p))
        n = input("Do you want too continue? (y/n): ").lower()
        if n == "n":
            exit()
        else:
            play(p=1)

    if p == 1:
        p = 2
    else:
        p = 1
    play(p)

if __name__ == "__main__":
    play(p=1)
