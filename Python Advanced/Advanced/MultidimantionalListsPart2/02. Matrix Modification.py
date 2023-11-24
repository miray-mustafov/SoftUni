matrix_size=int(input())
matrix=[]
for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])
while True:
    command=input()
    if command=="END":
        break
    add_substr,x,y,num=command.split()
    x=int(x)
    num = int(num)
    y = int(y)
    if x<0 or x>=matrix_size or y<0 or y>=matrix_size:
        print('Invalid cooordinates')
        continue
    if add_substr=='Add':
        matrix[x][y]+=num
    elif add_substr=='Subtract':
        matrix[x][y] -= num


for row in matrix:
    print(*row,sep=' ')





