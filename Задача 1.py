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
