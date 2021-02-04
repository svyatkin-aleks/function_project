def inverse(func):
    def inversion(*args):
        print(f'Должно было получиться:')
        func(*args)
        args = args[::-1]
        print('А получилось:')
        return func(*args)
    return inversion

@inverse
def full_name(first_name, middle_name, last_name):
    print(f'{first_name} {middle_name} {last_name}')

full_name('Alexei', 'Vladzimirovich', 'Svyatkin')

@inverse
def exponent(a,b):
    print(a ** b)

exponent(5, 2)

