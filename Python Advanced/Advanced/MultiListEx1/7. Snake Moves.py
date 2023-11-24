

# from collections import deque
# n,m=[int(x) for x in input().split()]
# txt=input()
# size=len(txt)
#
# i=0
# row_elmts=deque()
# for row in range(n):
#     row_elmts.clear()
#     if row%2==0:
#         for _ in range(m):
#             row_elmts.append(txt[i%size])
#             i+=1
#     else:
#         for _ in range(m):
#             row_elmts.appendleft(txt[i%size])
#             i+=1
#
#     print(''.join(row_elmts))
