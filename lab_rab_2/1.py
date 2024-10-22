#!/usr/bin/env python3
import re
import sys

def is_valid_name(name):
    """
    Функция для проверки валидности имени.
    Имя должно начинаться с заглавной буквы и содержать только буквы.
    """
    if not name[0].isupper():
        return False
    if not re.match("^[A-Za-zА-Яа-яёЁ]+$", name):
        return False
    return True

def greet_names_from_file(input_file, error_file):
    """
    Режим 1: Приветствие имён из файла и запись ошибок в файл.
    """
    try:
        with open(input_file, 'r') as file:
            names = file.readlines()

        with open(error_file, 'w') as error_log:
            for name in names:
                name = name.strip()
                if is_valid_name(name):
                    print(f"Привет, {name}!")
                else:
                    error_log.write(f"Ошибка: Некорректное имя '{name}'\n")
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def greet_user_interactive():
    """
    Режим 2: Запрос имени у пользователя, с обработкой Ctrl+C.
    """
    try:
        while True:
            name = input("Введите ваше имя: ").strip()
            if is_valid_name(name):
                print(f"Привет, {name}!")
            else:
                print("Ошибка: Имя должно начинаться с заглавной буквы и содержать только буквы.")
    except KeyboardInterrupt:
        print("\nGoodbye!")  # Вывод прощального сообщения при прерывании процесса

def main():
    """
    Основная функция программы, определяющая режим работы.
    """
    if len(sys.argv) > 1:
        # Если есть аргумент, запускаем режим чтения из файла
        input_file = sys.argv[1]  # Имя файла передается как аргумент
        error_file = "error.txt"
        greet_names_from_file(input_file, error_file)
    else:
        # Если аргументов нет, запускаем интерактивный режим
        greet_user_interactive()

if __name__ == "__main__":
    main()
