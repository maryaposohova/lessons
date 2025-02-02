# Практическая работа по уроку "Организация программ и методы строк."
# Количество символов с пробелами
#my_string = len((input('Введите предложение или слово, а я подсчитаю сколько в нем всего символов: ')))
#print(my_string)
#Количество символов без пробелов, т.е. кол-во букв
#my_string = len((input('Введите предложение или слово, а я подсчитаю сколько в нем всего букв: ').replace(' ', '')))
#print(my_string)

# Практическая работа по уроку "Организация программ и методы строк."

# 1 читаем колво символов (с пробелом)
my_string = input('Введите предложение или слово: ')
print(len(my_string))

# 1а читаем колво символов (без пробела)
my_string = input('Введите предложение или слово: ')
print(len(my_string.replace(' ', '')))

#  2 перевод в верхний регистр
my_string = input('Введите предложение или слово: ')
print(my_string.upper())

# 3 перевод в нижний регистр
my_string = input('Введите предложение или слово: ')
print(my_string.lower())

# 4 удаляем все пробелы
my_string = input('Введите предложение или слово: ')
print(my_string.replace(' ', ''))

# 5 выводим первый символ строки
my_string = input('Введите предложение или слово: ')
print(my_string[0])

# 6 выводим первый символ строки
my_string = input('Введите предложение или слово: ')
print(my_string[-1])

''' ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/09/24 00:00|Практическая работа по уроку "Организация программ и методы строк".
Практическая работа по уроку "Организация программ и методы строк."

Цель: Написать программу на языке Python с использованием Pycharm для работы с методами строк и организации программ.

1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_4.py' и напишите весь код в нём.

2. Организуйте программу:
Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
Вывести количество символов введённого текста
3. Работа с методами строк:
Используя методы строк, выполните следующие действия:
Выведите строку my_string в верхнем регистре.
Выведите строку my_string в нижнем регистре.
Измените строку my_string, удалив все пробелы.
Выведите первый символ строки my_string.
Выведите последний символ строки my_string.
Примечания:
Для вывода значений на экран используйте функцию print().
Для вызова методов строк используйте операцию точки '.'.
Дополнительно о всех методах строк можно узнать здесь.
Пример результата выполнения программы:

Код:
name = input()
print(name.upper())

Ввод в консоль:
Urban

Вывод на консоль:
URBAN

Напишите код к домашнему заданию в ответе (комметарии).

Успехов!

https://github.com/maryaposohova/lesson0/blob/main/module_1_4.py'''

