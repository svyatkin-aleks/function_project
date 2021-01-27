def factorial(a):
    b = 1
    for i in range(1, a + 1):
        b *= i
    return b
print(factorial(5))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
def my_format(string, char='!'):
    result_string = f'{char}{string}{char}'
    return result_string
print(my_format("asdsa"))
def print_list(*args):
    print(args)
print_list(1,2,3,4,5)

