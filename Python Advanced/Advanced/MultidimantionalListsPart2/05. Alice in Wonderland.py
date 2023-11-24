n=int(input())
matrix=[]
a_row=0
a_col=0
for row in range(n):
    line=input().split()
    matrix.append(line)
    for col in range(n):
        if line[col] =="A":
            a_row,a_col=row,col
        elif line[col]=="R":
            r_row,r_col=row,col


def alice_moves(direction, a_row, a_col):
    if direction == "up":
        return a_row-1,a_col
    if direction == "down":
        return a_row+1,a_col
    if direction == "left":
        return a_row,a_col-1
    if direction == "right":
        return a_row, a_col + 1
teas=0
directions=("up",'left','right','down')
while True:
    direction=input()
    if direction not in directions:
        print("Alice didn't make it to the tea party.")
        matrix[a_row][a_col] = "*"
        break
    matrix[a_row][a_col]="*"
    a_row,a_col=alice_moves(direction,a_row,a_col)
    next_symbl=matrix[a_row][a_col]

    if a_row<0 or a_col<0 or a_col>=n or a_row>=n:
        print("Alice didn't make it to the tea party.")
        break
    if next_symbl=="R":
        print("Alice didn't make it to the tea party.")
        matrix[a_row][a_col]="*"
        break
    if next_symbl.isdigit():
        teas+=int(next_symbl)
        if teas>=10:
            matrix[a_row][a_col] = "*"
            print(f"She did it! She went to the party.")
            break

for row in matrix:
    print(*row)