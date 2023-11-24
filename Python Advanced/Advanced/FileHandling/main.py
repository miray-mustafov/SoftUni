from re import findall
from string import punctuation
with open("text.txt", 'r') as text:
    text=text.readlines()
    for row,line in enumerate(text):
        letts=len(findall('[A-Za-z]',line))
        psymbls=len(findall(r'[!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~]',line))

        with open("output.txt",'a') as file:
            file.write(line)
