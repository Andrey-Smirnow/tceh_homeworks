# 1. Написать функцию, которая спрашивает пользователя число и степень числа, возвращает число в степени.

a, n = float(input('Число - ')), float(input('Степень - '))


def exp(a, n):
    return a ** n


print('{} в {} степени = {}'.format(a, n, exp(a, n)))

# 2. Написать функцию для определения НОК(наименьшее общее кратное) для двух чисел.

a = int(input('a='))
b = int(input('b='))


def gcd(a, b):
    """Finding NOD"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mcd(a, b):
    """Finding NOK"""
    return (a / gcd(a, b)) * b


print(mcd(a, b))

# 3. Написать функцию, которая принимает список, и возвращает словарь в формате: "тип данных: количество объектов"
#    count_types([1, 4, 'd']) -> {<class 'int'>: 2, <class 'str'>: 1}

my_list = [55, 'f', 3, 'a']
my_dict = {}

count_str, count_int, count_float = 0, 0, 0


def count_types(my_list):
    global count_str, count_int, count_float
    for i in my_list:
        if type(i) == str:
            count_str += 1
            my_dict[type(i)] = count_str
        elif type(i) == int:
            count_int += 1
            my_dict[type(i)] = count_int
        elif type(i) == float:
            count_float += 1
            my_dict[type(i)] = count_float
    return my_dict


print('Считаем типы данных в списке {}: '.format(my_list))

print(count_types(my_list))

# 4. Написать функцию, которая принимает два словаря, сравнивает их ключи, выдает в консоль сколько у них общих ключей

my_d1 = {5: 'abc', 1: 'eee', 2: 'ttt'}
my_d2 = {5: 'bbb', 4: 'ddd', 3: 'aaa'}


def count_k(my_d1, my_d2):
    return len(my_d1.keys() and my_d2.keys())


print('Общих ключей : {}'.format(count_k(my_d1, my_d2)))


# 5. Написать функцию, которая принимает любое количество аргументов, она вернуть список типов, принятых аргументов
#                             find_types(1, 's', []) -> [<class 'int'>, <class 'str'>, <class 'list'>]
def find_types(*n):
    list_types = []
    for i in n:
        list_types.append(type(i))
    return list_types


print('Cписок типов принятых аргументов функции:')
print(find_types(1, 'aaaa', [1, 15], {'1': '1', }, 77))

# 6. Написать функцию, которая принимает на вход список списков (матрицу)
# и выводит ее в виде матрицы (один ряд на одной строке) в консоль
my_matrix = [
    [33, 55, 66, 777],
    ['abc', 'def', 'ghi', 'mno'],
    ['d', 'i', 'n', 3, 85, 7]
]


def matrix_print(matrix):
    for row in matrix:
        print(row)


print('Вывожу матрицу:')
matrix_print(my_matrix)

# 7. Написать функцию, которая принимает любое количество аргументов -
#     списков, она должна возвращать список из всех объектов списков, но каждый
#      объект должен быть уникальным join_lists([1, 2], ['a', 2], ['c', 1]) -> [1, 2, 'a', 'c']
list_1 = [1, 'b', 3, 4]
list_2 = [3, 4, 5, 6]
list_3 = [5, 6, 'a', 'b']


def join_lists(*lists):
    common_list = []
    for index in lists:
        for i in index:
            common_list.append(i)
    return list(set(common_list))


print('Уникальные объекты списков:')
print(join_lists(list_1, list_2, list_3))

