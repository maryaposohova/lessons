# numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# positive_numbers = []
#
# index = 0
# while index < len(numbers):
#     number = numbers[index]
#
#     if number < 0:
#         break  # Прерываем цикл при встрече отрицательного числа
#
#     if number == 0:
#         index += 1
#         continue  # Пропускаем 0 и переходим к следующему числу
#
#     positive_numbers.append(number)
#     index += 1
#
# print(positive_numbers)

rez = [42, 69, 322, 13, 99]
print(rez)

# Задача "Нули ничто, отрицание недопустимо!"

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_pos = []
ind = 0
while ind < len(my_list):
    #my_list = my_list[ind]  # мой список превратился в индекс по счетчику в списке
    if my_list[ind]< 0:
        break

    if my_list[ind] == 0:
        ind = ind +1
        continue

    elif my_list[ind] > 0:
        print(list_pos.append(my_list))
        ind = ind + 1

