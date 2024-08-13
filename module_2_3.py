# Задача "Нули ничто, отрицание недопустимо!"

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ind = 0
while ind < len(my_list):
    element = my_list[ind]
    if element == 0:
        ind = ind + 1
        continue
    if element < 0:
        ind = ind + 1
        break
    elif element > 0:
        ind = ind + 1
        print(element)