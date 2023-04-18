# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
from random import randint

n = int(input("Введите количество элементов множества 1   "))
m = int(input("Введите количество элементов множества 2   "))
arr_a = []
arr_b = []
for i in range(n):
    arr_a.append(randint(0, 10))
    
#print(arr_a)

for i in range(m):
    arr_b.append(randint(0, 10))
    
#print(arr_b)

set_a = set(arr_a)
set_b = set(arr_b)

print(set_a)
print(set_b)

set_c = set_a.intersection(set_b)
#print(set_c)

arr_c = list(set_c)
#print(arr_c)

for i in range(len(arr_c)-1):
    index_min = i
    for j in range(i + 1,len(arr_c)):
        if arr_c[j] < arr_c[index_min]:
            index_min = j
            
    temp = arr_c[i]
    arr_c[i] = arr_c[index_min]
    arr_c[index_min] = temp
       
    
    
print(*arr_c)
    
        
    
    




    

