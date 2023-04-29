# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


def Simple(n):
    if n < 2:
        return "Нет"
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return "Нет"
        return "Да"



print(Simple(int(input("Введите число :"))))


print(*{i if Simple(i) == "Да" else '' for i in range(int(input("Введите число :")))})