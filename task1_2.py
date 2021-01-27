def factorial(a):
    b = 1
    for i in range(1, a + 1):
        b *= i
    return b
print(factorial(4))