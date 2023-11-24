def print_triangle(n):
    for rwi in range(1,n+1):
        for digit in range(1,rwi+1):
            print(digit,end=' ')
        print()

    for rwi in range(n-1, 0,-1):
        for digit in range(1,rwi+1):
            print(digit,end=' ')
        print()