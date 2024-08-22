# Задание "Слишком древний шифр"

n = 5
list_ = ""

for i in range(1, n):
    for j in range(i + 1, n):
        sum_ = i + j
        if n % sum_ == 0:
            list_ = list_ + f'{i}{j}'

print(list_)

