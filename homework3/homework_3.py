
#   Задача 1. Написать функцию, которая выбрасывает одно из трех исключений: ValueError, TypeError или RuntimeError
#    случайным образом. В месте вызова функции обрабатывать все три исключения


import random


def random_except():
    raise random.choice([ValueError, TypeError, RuntimeError])


try:
    random_except()
except ValueError:
    print('Ошибка!  ValueError')
except TypeError:
    print('Ошибка!   TypeError')
except RuntimeError:
    print('Ошибка!   RuntimeError')

#    Задача 2. Написать функцию, которая принимает на вход список, если в списке все объекты - int, сортирует его.
#    Иначе выбрасывает ValueError.


def sort_list(*args):
    try:
        for arg in args:
            if type(arg) != int:
                raise ValueError()
        new_list = sorted(args)
        print('Sorted list: ', *new_list)

    except ValueError as e:
        print('Not all int in List', e)


sort_list(1, 3, 4, 5, 12, 11)
sort_list('String', 1, 3, 4, 5, 12, 11)


#    Задача 3. Написать функцию, которая принимает словарь, преобразует все ключи словаря к строкам и возвращает
#    новый словарь.


def str_keys(diction):
    return dict(zip([str(i) for i in diction.keys()], [diction[i] for i in diction]))

print(str_keys({1: 2, 3: 4, 5: 6}))
print(str_keys({(1, 0, ): 2, (3, 11, ): 4, (5, 3, ): 6}))
print(str_keys({None: 1}))


#    Задача 4. Написать функцию, которая принимает список чисел и возвращает их произведение


def m_list(value):
    x = 1
    for i in value:
        x *= i
    return x

list_num = (1, 4, 2)
print(m_list(list_num))


# Задача 5. Написать три функции: do_work, handle_success, handle_error. do_word(my_list, success_callback,
# error_callback) принимает на вход три аргумента: список, функцию для обработки успеха и функцию для обработки ошибки.
# Ее задача проверить, что все значения в списке идут по-возрастанию. Если все верно: вызываем success_callback, иначе:
# error_callback. Функция handle_success пишет в консоль информацию об успешном выполнении. Функция handle_error
# выбрасывает ValueError


def do_work(my_list, success_callback, error_callback):
    if my_list == sorted(my_list):
        return success_callback()
    else:
        return error_callback


def handle_success():
    print("List is sorted!")


def handle_error():
    raise ValueError("List wast sorted.")


list1 = [1, 8, 9, 12]
print(do_work(list1, handle_success, handle_error))

