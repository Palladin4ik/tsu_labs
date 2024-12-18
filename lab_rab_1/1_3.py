#!/usr/bin/env python3
import sys
import math

try:
    data = input()
    A = float(data)

    if A < 0:
        raise ValueError("Нельзя вычислить квадратный корень из отрицательного числа!")

    result = math.sqrt(A)

    with open("output.txt", "w") as file:
        file.write(f"Квадратный корень числа {A}: {result}\n")

    print("Результат записан в файл output.txt")
except ValueError as ve:
    with open("error.txt", "a") as error_file:
        error_file.write(f"Ошибка преобразования данных в число: {ve}\n")
    print(f"Ошибка: {ve}", file=sys.stderr)
except IOError as ioe:
    with open("error.txt", "a") as error_file:
        error_file.write(f"Ошибка записи в файл: {ioe}\n")
    print(f"Ошибка записи в файл: {ioe}", file=sys.stderr)
except Exception as e:
    with open("error.txt", "a") as error_file:
        error_file.write(f"Ошибка: {e}\n")
    print(f"Ошибка: {e}", file=sys.stderr)
