def valididxs(i, j):
    if 0<=i<n and 0<=j<n:
        return True
    return False

def collisions(table, i, j):
    collisions = 0
    if valididxs(i + 2, j + 1) and table[i + 2][j + 1] == k:
        collisions+=1
    if valididxs(i + 2, j - 1) and table[i + 2][j - 1] == k:
        collisions+=1
    if valididxs(i - 2, j + 1) and table[i - 2][j + 1] == k:
        collisions+=1
    if valididxs(i - 2, j - 1) and table[i - 2][j - 1] == k:
        collisions+=1
    if valididxs(i + 1, j + 2) and table[i + 1][j + 2] == k:
        collisions+=1
    if valididxs(i + 1, j - 2) and table[i + 1][j - 2] == k:
        collisions+=1
    if valididxs(i - 1, j + 2) and table[i - 1][j + 2] == k:
        collisions+=1
    if valididxs(i - 1, j - 2) and table[i - 1][j - 2] == k:
        collisions+=1
    return collisions


def knightsToRemove():
    global n
    n = int(input())
    if n < 3:
        return 0

    table = []
    for i in range(n):
        table.append(list(input()))
    global o
    o='0'
    global k
    k='K'

    removed_kn=0
    kon_sblysyci={}

    while True:
        maxSbl = 0
        for i in range(n):  # todo counting each knight collisions
            for j in range(n):
                if table[i][j] == k:
                    acount=collisions(table, i, j)
                    if not acount == 0:
                        kon_sblysyci[(i, j)]=acount
                        if kon_sblysyci[(i, j)] > maxSbl:
                            maxSbl = kon_sblysyci[(i, j)]
        if len(kon_sblysyci)==0:
            break
        # todo Removing the kon with max sblysyci
        for kon, sblysyci in kon_sblysyci.items():
            if sblysyci == maxSbl:
                kon_sblysyci.pop(kon)
                table[kon[0]][kon[1]] = o
                removed_kn += 1
                break


        # nocolossions=True
        # for kon,sblysyci in kon_sblysyci.items():
        #     if sblysyci!=0:
        #         nocolossions=False
        # if nocolossions==True:
        #     break
        kon_sblysyci.clear()
    return removed_kn

print(knightsToRemove())