#!/usr/bin/env python3
import sys
import random

try:
    A = int(input("Введите число A: "))
    B = random.randint(-10, 10)
    
    result = A / B
    
except ValueError as e:
    # Логирование ошибки в файл
    with open("error.txt", "a") as error_file:
        error_file.write(f"Ошибка преобразования данных в число: {e}\n")
    print("Ошибка: неверное значение A", file=sys.stderr)
except ZeroDivisionError as e:
    # Логирование ошибки в файл
    with open("error.txt", "a") as error_file:
        error_file.write(f"Ошибка деления: делитель равен нулю: {e}\n")
    print("Ошибка: деление на ноль!", file=sys.stderr)
else:
    print(result)  # Вывод результата, если ошибок не произошло
