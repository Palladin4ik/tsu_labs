#!/usr/bin/env python3
import random

try:
    A = random.randint(-10, 10)
    print("Число A:", A)
except Exception as e:
    import sys
    print(f"Ошибка: {e}", file=sys.stderr)
