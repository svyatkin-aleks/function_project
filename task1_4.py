def my_func(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
    a = args[0]
def my_func1(*args):
    a = args[0]
    for i in args[1:]:
        if i > a:
            a = i
    return a
    print(k)
print(my_func(1, 2, 3, 4))
print(my_func1(1, 2, 3, 50))