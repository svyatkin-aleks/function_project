def my_func(**names):
    for key, value in names.items():
        if len(key) %2 == 0:
            print(value)

my_func(lesha = 1, maksim = 2, anton = 3, grisha = 4)


def sr_arifm(*args):
    sum = 0
    for i in args:
        sum += i
    sr_arifm = sum / len(args)
    return sr_arifm
print(sr_arifm(2, 3, 3, 4))
def sr_geometr(*args):
    proizvedenie = 1
    for i in args:
        proizvedenie *= i
    sr_geometr = proizvedenie / len(args)
    return sr_geometr
print(sr_geometr(2, 3, 4))
def mean_type(*args, mean_type):
    if mean_type == 1:
        print(sr_arifm(*args))
    elif mean_type == 2:
        print(sr_geometr(*args))
mean_type(2, 4, 3, mean_type= 2)