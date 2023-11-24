def cookie(matrix, c_row, c_col):
    global left_presents_count
    global nice_kids_left
    matrix[c_row][c_col] = '-'     #todo !!!!--------------
    for direc in directions:
        side_row,side_col=move_next_house(direc, c_row, c_col)
        if not valid(side_row,side_col):
            continue

        if matrix[side_row][side_col]=="V" or matrix[side_row][side_col]=="X":
            left_presents_count-=1
            if matrix[side_row][side_col]=="V":
                nice_kids_left-=1
        elif matrix[side_row][side_col]=="C":
            matrix,left_presents_count,nice_kids_left=cookie(matrix,side_row,side_col)

        matrix[side_row][side_col]='-'
        if left_presents_count==0:
            return matrix,left_presents_count,nice_kids_left
    return matrix,left_presents_count,nice_kids_left


def move_next_house(direction,row,col):
    if direction=="up":
        return row-1,col
    if direction=="down":
        return row+1,col
    if direction=="right":
        return row,col+1
    if direction=="left":
        return row,col-1

def valid(row,col):
    return 0<=row<size and 0<=col<size
#todo------Excluding Edge Cases-------------------------------------------------------------------------------------------------------------------
# print(*matrix,sep='\n')
# print(santa_row,santa_col)
# print(nice_kids_count)
#todo-------------------------------------------------------------------------------------------------------------------------

all_presents_count=int(input())
global left_presents_count
left_presents_count=all_presents_count
global size
size=int(input())
matrix=[]

nice_kids_count=0
santa_row=0
santa_col=0
for row in range(size):
    row_elements=input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col]=='V':
            nice_kids_count+=1
        elif row_elements[col]=="S":
            santa_row=row
            santa_col=col

global nice_kids_left
nice_kids_left=nice_kids_count

global directions
directions=["down","up","right","left"]
while True:
    direction=input()
    if direction=="Christmas morning" or direction=='':
        break
    matrix[santa_row][santa_col] = '-'

    santa_row, santa_col=move_next_house(direction, santa_row, santa_col)
    if not  valid(santa_row, santa_col):
        continue

    if matrix[santa_row][santa_col]== "V":
        left_presents_count-=1
        nice_kids_left-=1
    elif matrix[santa_row][santa_col]== "C":
        matrix,left_presents_count,nice_kids_left=cookie(matrix, santa_row, santa_col)

    matrix[santa_row][santa_col] = 'S'

    if left_presents_count==0 and nice_kids_left>0:
        print("Santa ran out of presents!")
        break


for line in matrix:
    print(*line)
if nice_kids_left>0:
    print(f"No presents for {nice_kids_left} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.")

