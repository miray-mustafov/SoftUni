def fill_the_box(*args):
    space=args[0]*args[1]*args[2]
    i=3
    while args[i]!="Finish":
        space-=args[i]
        if space<=0:
            hihi=sum(args[i+1:len(args)-1])-space
            return (f"No more free space! You have {hihi} more cubes.")
        i+=1
    return f"There is free space in the box. You could put {space} more cubes."

