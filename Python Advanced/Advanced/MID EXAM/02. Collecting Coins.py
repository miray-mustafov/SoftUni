size=int(input())
matrix=[]
p_row=0
p_col=0
for rowindx in range(size):
    line=input().split()
    if "P" in line:
        p_row,p_col=rowindx,line.index("P")
    for i in range(size):
        if line[i].isdigit():
            line[i]=int(line[i])
    matrix.append(line)

path=[[p_row,p_col]]
coins=0
while True:
    matrix[p_row][p_col]=0
    direction=input()
    if direction=="up":
        next_row,next_col=(p_row-1)%size,p_col
    elif direction=="down":
        next_row, next_col = (p_row+1)%size,p_col
    elif direction=="left":
        next_row, next_col = p_row,(p_col-1)%size
    elif direction=="right":
        next_row, next_col = p_row,(p_col+1)%size
    else:
        break
    path.append([next_row,next_col])

    if matrix[next_row][next_col]=="X":
        print(f"Game over! You've collected {coins//2} coins.")
        break
    coins+=matrix[next_row][next_col]
    if coins>=100:
        print(f"You won! You've collected {coins} coins.")
        break


    p_row,p_col=next_row,next_col

print("Your path:")
print(*path,sep='\n')