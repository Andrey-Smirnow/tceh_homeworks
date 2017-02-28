# 1. Написать списковые выражения, которые:
# создают список из строк всех нечетных чисел от 1 до 100
# создают список из объектов другого списка, кроме итерируемых
# создают список из фразы 'The quick brown fox jumps over the lazy dog',
# где каждый объект списка - кортеж из: слова в верхнем регистре, слова в
# случанйном регистре (qUIcK) и длины слова

# 1.1 создают список из строк всех нечетных чисел от 1 до 100
import collections
m = [i for i in range(1,100) if i % 2 !=0]
print(m)

# 1.2 создают список из объектов другого списка, кроме итерируемых  ??  Как понять кроме итерируемых ??
my_list1 = [1,2,3,'r','a','1,2','2',False]
my_list2 = [i for i in my_list1 if not isinstance(i, collections.Sequence)] # ?? Как работает collections.Sequence ??
print(my_list1)
print(my_list2)

# 1.3 создают список из фразы 'The quick brown fox jumps over the lazy dog',
# где каждый объект списка - кортеж из: слова в верхнем регистре,
# слова в случанйном регистре (qUIcK) и длины слова
import random
my_list3 = 'The quick brown fox jumps over the lazy dog'
my_list4 = [(str.upper(c), ''.join([random.choice([str.upper(d),str.lower(d)]) for d in c]), len(c)) for c in my_list3.split(' ')]

# Метод ''.join преобразует список в строку без разделителя (т.к. <<<<''>>>>.join)
# Не понятен смысл 'for d in c'

print(my_list4)
