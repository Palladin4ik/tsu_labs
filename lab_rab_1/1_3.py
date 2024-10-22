#!/usr/bin/env python3
import math

try:
    A = float(input("Введите число для вычисления квадратного корня: "))
    
    if A < 0:
        raise ValueError("Нельзя вычислить квадратный корень из отрицательного числа!")
    
    result = math.sqrt(A)
    
    with open("output.txt", "w") as file:
        file.write(f"Квадратный корень числа {A}: {result}\n")
    
    print("Результат записан в файл output.txt")
except ValueError as ve:
    print(f"Ошибка: {ve}", file=sys.stderr)
except IOError as ioe:
    print(f"Ошибка записи в файл: {ioe}", file=sys.stderr)
except Exception as e:
    print(f"Ошибка: {e}", file=sys.stderr)
