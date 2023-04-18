# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint 

n = int(input("Введите количество элементов массива   "))
x = int(input("Введите искомое число   "))

list_1 = []

for i in range(n):
    list_1.insert(i, randint(-10, 10))
print(list_1)

dif_min = abs(x - list_1[0])
near_pos = list_1[0]
for i in range(1, n):
    if abs(x - list_1[i]) < dif_min:
        dif_min = abs(x - list_1[i])
        near_pos = list_1[i]
        
print(near_pos)
