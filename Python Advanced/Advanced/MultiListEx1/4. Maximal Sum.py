import sys
rows,cols=[int(b) for b in input().split()]
matrix=[]

for row in range(rows):
    matrix.append([int(n) for n in input().split()])


def takeSumFromElmtsIn3x3Square(row, col, matrix):
    return matrix[row][col]+matrix[row][col+1]+matrix[row][col+2]+ \
           matrix[row+1][col]+matrix[row+1][col+1]+matrix[row+1][col+2]+ \
           matrix[row+2][col]+matrix[row+2][col+1]+matrix[row+2][col+2]

maximal_sum=-sys.maxsize

for row in range(rows-2):
    for col in range(cols-2):

        curr_sum=takeSumFromElmtsIn3x3Square(row,col,matrix)
        if maximal_sum<curr_sum:
            maximal_sum=curr_sum
            max_row=row
            max_col=col

print(f"Sum = {maximal_sum}")
for row in range(max_row,max_row+3):
    for col in range(max_col,max_col+3):
        print(matrix[row][col], end=' ')
    print()