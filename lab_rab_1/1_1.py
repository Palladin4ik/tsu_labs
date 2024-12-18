#!/usr/bin/env python3
import sys
import random

try:
    A = random.randint(-10, 10) #Генерация случайного числа
    print("Число A:", A) #Вывод числа A
except Exception as e: #Запись ошибок в файл error.txt
    with open("error.txt", "a") as error_file:
        error_file.write(f"Ошибка в 1_1.py: {e}\n")
