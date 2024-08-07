# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

# кортеж
immutable_var = 1, 2, "a", True
print(immutable_var)

# в составе кортежа нельзя заменить символы, потому что создан быть неизменяемым и не поддерживает
# обращения по элементуам, но можно поменять символы в составе списка, входящего в кортеж
immutable_var = 1, 2, "a", True, [3,3]
immutable_var[4][0] = '5', 6, [44]
print(immutable_var)

# список
mutable_list =[1, 2, "a", True, 'Modified']
print(mutable_list)