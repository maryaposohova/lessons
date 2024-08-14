# Задача "Всё не так уж просто":

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []

for i in range(1, len(numbers)):
    element = numbers[i]
    is_prime = True
    for j in range(2, element):
        if element % j == 0:
            is_prime = False
            break
    if is_prime:  # это тру, число простое
        prime.append(element)
    else:
        not_prime.append(element)
print(prime)
print(not_prime)




