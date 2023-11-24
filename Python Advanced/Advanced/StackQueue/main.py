


# n=int(input())
# codes=set()
# for _ in range(n):
#     code=input()
#     codes.add(code)
# whocame=set()
# code=input()
#
# while code!="END":
#     whocame.add(code)
#     code=input()
# whodidnt=codes-whocame
# whodidnt=sorted(whodidnt)
# print(len(whodidnt))
# print(*whodidnt,sep='\n')




# n=int(input())
# data=input()
# cars=set()
# for _ in range(n):
#     direction, carnum=data.split(', ')
#     if direction =='IN':
#         cars.add(carnum)
#     elif direction=="OUT" and carnum in cars:
#         cars.remove(carnum)
#
#     data=input()
#
# if cars:
#     print(*cars,sep='\n')
# else:
#     print(f"Parking Lot is Empty")