def funct(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i] * i
    return sum
print(funct(3, 4, 5))