#!/usr/bin/env python3
import random

try:
    A = int(input("Введите число A: "))
    B = random.randint(-10, 10)

    if B == 0:
        raise ZeroDivisionError("Деление на ноль!")
    
    result = A / B
    print(f"Число B: {B}")
    print(f"Результат A / B: {result}")
except ZeroDivisionError as zde:
    print(f"Ошибка: {zde}", file=sys.stderr)
except ValueError:
    print("Ошибка: некорректный ввод числа A!", file=sys.stderr)
except Exception as e:
    print(f"Ошибка: {e}", file=sys.stderr)
