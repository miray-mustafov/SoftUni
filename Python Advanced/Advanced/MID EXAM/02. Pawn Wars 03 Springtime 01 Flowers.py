

chess_board=[]
w_row=0
w_col=0
b_row=0
b_col=0
digit_letter={0:'a',1:'b',2:'c',3:'d',4:"e",5:'f',6:'g',7:'h'} #todo COLS


for rowi in range(8):
    line=input().split()
    if "b" in line:
        b_row,b_col=rowi,line.index("b")
    elif "w" in line:
        w_row,w_col=rowi,line.index('w')
    chess_board.append(line)

global capture

def white_can_capture(row, col, chess_board):
    global capture
    if col-1>=0 and chess_board[row-1][col-1]=='b':
        capture=[row-1,col-1]
        return True
    elif col+1<8 and chess_board[row-1][col+1]=='b':
        capture=[row-1,col+1]
        return True
    return False

def black_can_capture(row, col, chess_board):
    global capture
    if col-1>=0 and chess_board[row+1][col-1]=='w':
        capture=[row+1,col-1]
        return True
    elif col+1<8 and chess_board[row+1][col+1]=='w':
        capture = [row + 1, col + 1]
        return True
    return False
white_pawn_pos=None
black_pawn_pos=None
if abs(w_col-b_col)>1:#todo toest ako figurite sa na raztoqnie > ot 1 col smqtame ostavashtite hodove
    if w_row<=7-b_row:
        white_pawn_pos=f"{digit_letter[w_col]}8"
        print(f"Game over! White pawn is promoted to a queen at {white_pawn_pos}.")
    else:
        black_pawn_pos=f"{digit_letter[b_col]}1"
        print(f"Game over! Black pawn is promoted to a queen at {black_pawn_pos}.")
else:
    while True:
        if white_can_capture(w_row,w_col,chess_board):
            white_pawn_pos=f"{digit_letter[capture[1]]}{8-capture[0]}"
            print(f"Game over! White win, capture on {white_pawn_pos}.")
            break
        else:
            chess_board[w_row][w_col] = '-'
            w_row -= 1
            chess_board[w_row][w_col] = 'w'

        if black_can_capture(b_row,b_col,chess_board):
            black_pawn_pos = f"{digit_letter[capture[1]]}{8 - capture[0]}"
            print(f"Game over! Black win, capture on {black_pawn_pos}.")
            break
        else:
            chess_board[b_row][b_col] = "-"
            b_row += 1
            chess_board[b_row][b_col] = "b"