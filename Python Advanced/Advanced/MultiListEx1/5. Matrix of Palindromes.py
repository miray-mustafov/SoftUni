rows,cols=[int(b) for b in input().split()]
matrix=[]

for i in range(rows):
    for j in range(cols):
        print(f"{chr(ord('a')+i)}{chr(ord('a')+i+j)}{chr(ord('a')+i)}", end=' ')
    print()