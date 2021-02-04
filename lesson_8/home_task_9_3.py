def delete_even(func):
    def delete():
        result = list(filter(lambda x: x % 2 != 0, func()))
        print(result)
        return result

    return delete

@delete_even
def list_numbers():
    list = [i for i in range(20)]
    return list

list_numbers()

# SECOND METHOD
# def delete_even(func):
#     def delete():
#         result = func()
#         for i in result:
#             if i % 2 == 0:
#                 result.remove(i)
#         print(result)
#         return result
#
#     return delete
#
# @delete_even
# def list_numbers():
#     list_user = [int(input('Please enter number ')) for i in range(int(input('Please, enter len your list \n')))]
#     return list_user
#
# list_numbers()

