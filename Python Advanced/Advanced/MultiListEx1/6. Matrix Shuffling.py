def indx_isvalid(i1,i2,q1,q2,rows,cols):
    if 0<=i1<rows and 0<=i2<cols and 0<=q1<rows and 0<=q2<cols:
        return True
    print("Invalid input!")
    return False

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=' ')
        print()

n,m=[int(num) for num in input().split()]
matrix=[]
for i in range(n):
    matrix.append(input().split())

line=input()
while line!= "END":
    line=line.split()
    if len(line)!=5 or not line[0]=="swap":
        print("Invalid input!")
        line=input()
        continue

#todo check if indxes are digits----------------------------------------------------------------------------------------
    i1,i2,q1,q2=line[1:]
    if not i1.isdigit() or not i2.isdigit() or not q1.isdigit() or not q2.isdigit():
        print("Invalid input")
        continue
    else:
        i1, i2, q1, q2 = [int(x) for x in line[1:]]

#todo check if indx are valid----------------------------------------------------------------------------------------------
    if not indx_isvalid(i1, i2, q1, q2, n, m):
        line = input()
        continue
    # here indxes are valid
    matrix[i1][i2], matrix[q1][q2] = matrix[q1][q2], matrix[i1][i2]
    print_matrix(matrix)

    line=input()