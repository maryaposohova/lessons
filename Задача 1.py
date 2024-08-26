# # Проверка
# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# print(set(grades[0]))
# # Проверка, вычислет среднее значение, но только если во множестве один список, а если не один, выходит ошибка.
# m = {3, 4, 5}
# l = list(m)
# s = sum(l)
# d = len(l)
# print(s/d)
#
#
# grades =[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # оценки
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}   # ученики
# grades_set = list([set(grades) for grades in grades])
# # middle_grape = sum(grades_set)/len(grades_set) # показывает ошибку(разные типы), приведение к float е помогли/
# dictionary = dict(zip(sorted(students), grades_set))
# print(dictionary)


# grades =[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # оценки
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}   # ученики
# grades_set = [set(grades) for grades in grades]
# grades_list = [list(s) for s in grades]
# midl_grades = sum(grades_list) / len(grades_list)
# dictionary = dict(zip(sorted(students), midl_grades))
# print(dictionary)
# print(type(grades))

# grades_set = [set(grades) for grades in grades]
# grades_list = [list(s) for s in grades]
# midl_grades = sum(grades_list) / len(grades_list)
# dictionary = dict(zip(sorted(students), midl_grades))
# print(dictionary)
# print(type(grades))

grades =[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # оценки
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}   # ученики
midl_grades = (sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
               sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4]))
dictionary = dict(zip(sorted(students), midl_grades))
print(dictionary)


''' ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/09/26 00:00|Дополнительное практическое задание по модулю*
Дополнительное практическое задание по модулю: "Базовые структуры данных."

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

Предисловие:
Сложность подобных задач заключается в:
Отсутствии чёткого алгоритма решения. Его вы должны придумать сами на основе полученных ранее знаний (синтаксиса и инструментов).
Объединении большинства тем изученного модуля.
Предполагаемом большом объёме решения.

Задание "Средний балл":
Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":

На вход даны следующие данные:
Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
Например: 'Aaron' - [5, 3, 3, 5, 4]
Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.

Вывод в консоль:
{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}


Примечания:
Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).


Напишите код к домашнему заданию в ответе (комметарии).

Успехов!

https://github.com/maryaposohova/lesson0/blob/main/Задача%201.py'''