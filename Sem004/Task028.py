# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def Sum(a, b):
    if a > 0 and b > 0:
        i = 2
        return i + Sum(a - 1, b - 1)
        
    elif (a <= 0 and b > 0) or (b <= 0 and a > 0):
        i = 1
        return i + Sum(a - 1, b - 1)
        
    elif a <= 0 and b <= 0:
        return 0
    
    
print(Sum(int(input("Введите число а :")), int(input("Введите число b :"))))  