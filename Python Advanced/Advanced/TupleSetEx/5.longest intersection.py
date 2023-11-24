def takerange(range):
    start,end=range.split(',')
    start=int(start)
    end=int(end)
    return set(range(start, end +1))

n=int(input())

for i in range(n):
    range1,range2=input().split('-')
    range1_set=takerange(range1)
    range2_set=takerange(range2)
    a=2
