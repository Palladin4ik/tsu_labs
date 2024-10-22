#!/usr/bin/env python3
import math

# Чтение числа A из stdin
A = float(input("Введите число для вычисления квадратного корня: "))

# Проверка, что число неотрицательное
if A < 0:
    result = "Ошибка: нельзя вычислить квадратный корень из отрицательного числа!"
else:
    # Вычисление квадратного корня
    result = math.sqrt(A)

# Запись результата в файл output.txt
with open("output.txt", "w") as file:
    file.write(f"Квадратный корень числа {A}: {result}\n")

print("Результат записан в файл output.txt")
