countSquares=0
rows,cols=[int(b) for b in input().split()]
matrix=[]
for row in range(rows):
    matrix.append(input().split())
for row in range(rows-1):
    for col in range(cols-1):
        if matrix[row][col]==matrix[row+1][col]==\
                matrix[row][col+1]==matrix[row+1][col+1]:
            countSquares+=1

print(countSquares)