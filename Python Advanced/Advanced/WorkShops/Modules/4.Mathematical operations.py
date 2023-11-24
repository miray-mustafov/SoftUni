from calcuations import *

operation_refs={'+' : sum_a_b,
                '-' : substract_a_b,
                '*' : multiply_a_b,
                '/' : divide_a_b,
                '^' : power_a_b}

a,operand,b=input().split()
a=int(a)
b=int(b)

try:
    result=operation_refs[operand](a,b)
    print(f"{result:.2f}")
except ZeroDivisionError:
    print("Cant divide by zero retard")


