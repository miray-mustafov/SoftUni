from collections import deque
kids=deque(input().split())
n=int(input())

while len(kids)>1:
    for num in range(1,n+1):
        if num%n==0:
            print(f"Removed {kids.popleft()}")
            break
        kids.append(kids.popleft())

print(f"Last is {''.join(kids)}")
# from collections import deque
# kids=deque(input().split())
# n=int(input())
# n=n-1
# while len(kids) !=1:
#     kids.rotate(-n)
#     print(f"Removed {kids.popleft()}")
# print(f"Last is {kids.pop()}")