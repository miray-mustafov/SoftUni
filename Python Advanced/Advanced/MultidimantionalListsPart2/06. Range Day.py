def get_next_pos(direction,row,col,steps):
    if direction=="up":
        return row-steps,col
    if direction=="down":
        return row+steps,col
    if direction=="right":
        return row,col+steps
    if direction=="left":
        return row,col-steps

def valid(row,col,size):
    return 0<=row<size and 0<=col<size

size=5
matrix=[]

targets_count=0
player_row=0
player_col=0
for row in range(size):
    row_elements=input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col]=='x':
            targets_count+=1
        elif row_elements[col]=="A":
            player_row=row
            player_col=col

n=int(input())
targets_coords=[]
for _ in range(n):
    command_args=input().split()
    command=command_args[0]
    direction=command_args[1]

    if command=='move':
        steps=int(command_args[2])
        next_row,next_col=get_next_pos(direction,player_row,player_col,steps)
        if not valid(next_row,next_col,size) or matrix[next_row][next_col]=='x':
            continue
        matrix[player_row][player_col]='.'
        player_row,player_col=next_row,next_col
        matrix[player_row][player_col]="A"
    else:
        bullet_row,bullet_col=player_row,player_col
        while True:
            bullet_row,bullet_col=get_next_pos(direction,bullet_row,bullet_col,1)
            if not valid(bullet_row,bullet_col,size):
                break
            if matrix[bullet_row][bullet_col]=='x':
                targets_coords.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col]='.'
                break
    if len(targets_coords)==targets_count:
        break

if len(targets_coords)==targets_count:
    print(f"Training completed! All {targets_count} targets hit.")
    print(*targets_coords,sep='\n')
else:
    print(f"Training not completed! {targets_count-len(targets_coords)} targets left.")
    if targets_coords:
        print(*targets_coords,sep='\n')