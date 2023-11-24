def concatenate(*args):
    sokem=""
    for arg in args:
        sokem+=arg
    return sokem


print(concatenate("I", " ", "Love", " ", "Python"))