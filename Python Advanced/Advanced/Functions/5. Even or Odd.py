def even_odd(*args):
    odeven=args[-1]
    args=[int(x) for x in args[:-1]]
    listt=[]
    parity=0 if odeven=="even" else 1
    for num in args:
        if num%2==parity:
            listt.append(num)
    return listt


print(even_odd(1, 2, 3, 4, 5, 6, "even"))