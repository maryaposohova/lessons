# Задача "Все ли равны?":

first = input('Введите 1-е число: ')
second = input('Введите 2-е число: ')
third = input('Введите 3-е число: ')

if first == second and second == third:
    print("3")
elif first == second or second == third or first == third:
    print("2")
else:
    print("0")
