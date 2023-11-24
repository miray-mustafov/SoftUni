from collections import deque

def f(vowels,consonants,flowers_to_find):
    while vowels and consonants:
        vow = vowels.popleft()
        con = consonants.pop()
        for i in range(len(flowers_to_find)):
            flower = flowers_to_find[i]
            if vow in flower:
                flowers_to_find[i]=flowers_to_find[i].replace(vow, '', 900)
            if con in flower:
                flowers_to_find[i]=flowers_to_find[i].replace(con, '', 900)

            if  flowers_to_find[i] =='':
                return i,vowels,consonants

    return -1,vowels,consonants

#todo------------------------------------------------------------------------------------

vowels=deque(input().split())
consonants=input().split()
flowers_to_find=["rose","tulip","lotus","daffodil"]
IndxTheMisingFlower=["rose","tulip","lotus","daffodil"]

indx,vowels,consonants=f(vowels,consonants,flowers_to_find)
if indx>=0:

    print(f"Word found: {IndxTheMisingFlower[indx]}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")