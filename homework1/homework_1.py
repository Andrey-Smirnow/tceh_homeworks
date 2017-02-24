# -*- coding: utf-8 -*-
counter = 0
name1 = input("Что обозначает тип данных None?")
if 'Ничего' == name1 or name1 == 'ничего':
    counter += 1
    print('Верный ответ.')
else:
    print('Неверный ответ.')
    
name2 = input("Как обозначается цикл с пред-условием?")
if name2 == 'While' or name2 == 'while':
    counter += 1
    print('Верный ответ.')
else:
    print('Неверный ответ.')
    counter=0
name3 = input("Как обозначается перебирающий цикл?")

if name3 == 'for' or name3 == 'For':
    counter += 1
    print('Верный ответ.')
else:
    print('Неверный ответ.')
name4 = input("Как обозначается Истина?")
if name4 == 'True' or name4 == 'true':
    counter += 1
    print('Верный ответ.')
else:
    print('Неверный ответ.')
name5 = input("Как обозначается Ложь?")
if name5 == 'False' or name5 == 'false':
    counter += 1
    print('Верный ответ.')
else:
    print('Неверный ответ.')
name6 = input("Как обозначается целый числовой тип?")
if name6 == 'Int' or name6 == 'int':
    counter += 1
    print('Верный ответ.')
else:
    print('Неверный ответ.')
name7 = input("Как обозначается дробный числовой тип?")
if name7 == 'Float' or name7 == 'float':
    counter += 1
    print('Верный ответ.')
else:
    print('Неверный ответ.')
name8 = input("Как обозначается комплексный  тип?")
if name8 == 'Complex' or name8 == 'Complex':
    counter += 1
    print('Верный ответ.')
else:
    print('Неверный ответ.')
name9 = input("Какая версия актуального релиза Pyton2?")
if name9 == '2.7' or name9 == '2,7':
    counter += 1
    print('Верный ответ.')
else:
    print('Неверный ответ.')
name10 = input("Какая версия актуального релиза Pyton3?")
if name10 == '3.0' or name10 == '3'or name10 == '3,0':
    counter += 1
    print('Верный ответ.')
else:
    print('Неверный ответ.')
    
print('Игра закончена. Количество верных ответов {} из 10'.format(counter))
