#!/usr/bin/env python3
import random

# Чтение числа A из stdin
A = int(input("Введите число A: "))

# Генерация случайного числа B в диапазоне [-10, 10]
B = random.randint(-10, 10)

# Проверка деления на ноль
if B == 0:
    print("Ошибка: деление на ноль!")
else:
    # Вычисление отношения A/B
    result = A / B
    # Вывод результата
    print(f"Число B: {B}")
    print(f"Результат A / B: {result}")
