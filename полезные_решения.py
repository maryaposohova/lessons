"""
помещение чисел в список
"""
# a = map(int, input().split())
# print(list(a))
#
# lst = []
# lst += map(int, input().split())
# print(lst)

"""
сортировка по возрастанию и убыванию
"""

lst = [52, 65, 64, 54, 68, 59, 42, 63]
#lst= list(map(int, input().split()))
#  по убыванию с распаковкой списка
print(*sorted(lst))
#  по убыванию с распаковкой списка
print(*sorted(lst, reverse=True))

