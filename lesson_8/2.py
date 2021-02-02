cars = [{'model' : 'bmw', 'vin' : 12323234, 'year' : 1994},
        {'model' : 'audi', 'vin' : 219883, 'year' : 2008},
        {'model' : 'mercedes', 'vin' : 4543534, 'year' : 2001}]
cars_new = [cars[i] for i in range(len(cars)) if cars[i]['year'] > 2000]
cars_new = [car for car in cars if car['year'] > 2000]
print(cars_new)

# name_list = ['alex', 'masha']
# hello = lambda name: [f'hello {i}' for i in name]
# print((hello(name_list)))

# list1 = [1,2,3,4,5,6]
# result = map(lambda x: x **2, list1)
# print(set(result))

# list1 = [1,2,3,4]
# result = map(lambda x: str(x), list1[::-1])
# print(list(result))

# result = filter(lambda x: x % 2 == 0, [1,2,3,4,5,6])
# print((list(result)))

# list1 = ['alex', 'ksuha']
# result = filter(lambda x: 'k' in x, list1)
# print(list(result))

from functools import reduce
items = [1, 2, 3, 4, 5, 6]
# items_kr3 = filter(lambda x: x % 3 == 0, items)
proizvedenie = reduce(lambda x, y: x * y, list(filter(lambda x: x % 3 == 0, items)))
print(proizvedenie)