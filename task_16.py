# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1
import random

number_N = int(input("Введите количество элементов в списке\n"))
number_X = int(input("Введите искомое число:\n"))

some_list = [random.randint(0, number_X + 2) for i in range(0, number_N)]

print(*some_list)
print(some_list.count(number_X))