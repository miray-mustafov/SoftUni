numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    number=input()
    if not number.isdigit():
        print("The variable must be an integer")
        line=input()
        continue

    number = int(number)
    numbers_dictionary[number_as_string] = number
    line = input()


line = input()
while line != "Remove":
    searched = line
    if searched not in numbers_dictionary:
        print(f"Number does not exist in dictionary")
        line= input()
        continue

    print(numbers_dictionary[searched])
    line=input()


line = input()
while line != "End":
    searched = line
    if searched in numbers_dictionary:
        del numbers_dictionary[searched]
    else:
        print(f"Number does not exist in dictionary")
    line=input()

print(numbers_dictionary)
