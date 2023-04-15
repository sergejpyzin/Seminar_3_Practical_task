# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5
import random

number_N = int(input("Введите число элементов в списке:\n"))
number_X = int(input("Введите искомое число:\n"))

some_list = [random.randint(0, 10) for i in range(number_N)]

print(*some_list)

min = abs(number_X - some_list[0])
number = some_list[0]

for i in range(1, number_N):
    if abs(number_X - some_list[i]) < min:
        min = abs(number_X - some_list[i])
        number = some_list[i]

print(number)