def func_executor(*args):
    result_list=[]
    for arg in args:
        func=arg[0]
        nums_tupple=arg[1]
        result_list.append(func(*nums_tupple))

    return result_list

def sum_numbers(*args):
    sum=0
    for num in args:
        sum+=num
    return sum

def multiply_numbers(*args):
    multi=1
    for num in args:
        multi*=num
    return multi


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
