from collections import deque

data=input().split('|')
stackk=deque()
for el in data:
    stackk.append(el.split())
for _ in range(len(stackk)):
    print(*(stackk.pop()),end=' ')
