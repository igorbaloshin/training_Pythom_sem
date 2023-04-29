# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

list = input("Вводим элементы через запятую :").split(',')
a = int(input("Введите начало диапазона :"))
b = int(input("Введите конец диапазона :"))


list_int_clean = []
for i in range(len(list)):
    list_int_clean.append(int(list[i].strip()))

print(list)

print(list_int_clean)

print([i for i in range(len(list_int_clean)) if (a <= list_int_clean[i] <= b) ])