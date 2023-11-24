dictt={}
import re
with open('words.txt') as file:
    words=file.read().split()
    # words=[x.lower() for x in words.split()]
    with open('input.txt') as file:
        file=file.read()
        for word in words:
            reg=fr'\b{word}\b'
            count=len(re.findall(reg,file,re.IGNORECASE))
            dictt[word]=count
tuples=sorted(dictt.items(), key=lambda kvp: (kvp[1],kvp[0]), reverse=True)
with open('output.txt','a') as outputfile:
    for word,count in tuples:
        outputfile.write(f"{word}: {count}\n")