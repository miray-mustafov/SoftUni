def is_inside(r, c):
    return 0 <= r < board_size and 0 <= c < board_size


def get_position(r, c):
    result = ""
    for i in range(board_size):
        if c == i:
            result += chr(i + 97)

    counter = board_size
    for i in range(board_size):
        if r == i:
            result += chr(counter + 48)
        counter -= 1
    return result


board_size = 8
current_white_row, current_white_col = 0, 0
current_black_row, current_black_col = 0, 0

chess_board = []
for row in range(board_size):
    row_elements = input().split()
    chess_board.append(row_elements)

    for col in range(board_size):

        if chess_board[row][col] == "w":
            current_white_row, current_white_col = row, col

        if chess_board[row][col] == "b":
            current_black_row, current_black_col = row, col

while True:
    if is_inside(current_white_row - 1, current_white_col - 1) \
            and chess_board[current_white_row - 1][current_white_col - 1] == "b":
        position = get_position(current_white_row - 1, current_white_col - 1)
        print(f"Game over! White win, capture on {position}.")
        break

    elif is_inside(current_white_row - 1, current_white_col + 1) \
            and chess_board[current_white_row - 1][current_white_col + 1] == "b":
        position = get_position(current_white_row - 1, current_white_col + 1)
        print(f"Game over! White win, capture on {position}.")
        break

    else:
        chess_board[current_white_row][current_white_col] = "-"
        current_white_row -= 1
        chess_board[current_white_row][current_white_col] = "w"

        if current_white_row == 0:
            position = get_position(current_white_row, current_white_col)
            print("Game over! White pawn is promoted to a queen at {}.".format(position))
            break

    if is_inside(current_black_row + 1, current_black_col - 1) \
            and chess_board[current_black_row + 1][current_black_col - 1] == "w":
        position = get_position(current_black_row + 1, current_black_col - 1)
        print("Game over! Black win, capture on {}.".format(position))
        break

    elif is_inside(current_black_row + 1, current_black_col + 1) \
            and chess_board[current_black_row + 1][current_black_col + 1] == "w":
        position = get_position(current_black_row + 1, current_black_col + 1)
        print("Game over! Black win, capture on {}.".format(position))
        break

    else:
        chess_board[current_black_row][current_black_col] = "-"
        current_black_row += 1
        chess_board[current_black_row][current_black_col] = "b"
        if current_black_row == board_size - 1:
            position = get_position(current_black_row, current_black_col)
            print("Game over! Black pawn is promoted to a queen at {}.".format(position))
            break