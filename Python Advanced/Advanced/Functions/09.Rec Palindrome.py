import time
start_time = time.time()

word=input()
# word2=list(reversed(word))
# if list(word)==word2:
#     print("Yes")
# else:
#     print("No")
ispalindrome=True
for i in range(len(word)//2):
    left=word[i]
    right=word[-1-i]
    if left!=right:
        ispalindrome=False
        break
if ispalindrome:
    print(f"{word} YES palindrome")
else:
    print(f"No")
print("--- %s seconds ---" % (time.time() - start_time))