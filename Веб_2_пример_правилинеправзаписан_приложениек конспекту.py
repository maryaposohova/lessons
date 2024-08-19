# Приложение к конспекту к вебу2 по проверки написи примеров со скобками

line = '((2-4)*(6-7))'

amount = 0
i = 0
while i < len(line):
    # print(i, line[i])   # вспомогательный принт
    if line[i] == '(':
        amount = amount + 1
    if line[i] == ')' and amount > 0:  # если ставлю < 0, то неправильно показывает
        amount = amount - 1

    i = i + 1
    # print(f'{amount = }')   #  справочный принт

if amount == 0 and ')(' not in line:
    print(True)
else:
    print(False)
