# 52_crazy_exception_handling.py

try:
    for i in range(3):
        try:
            1 / 0
        except ZeroDivisionError:
            raise ZeroDivisionError("Error: You divided by zero!")
        finally:
            print("Finally executed")
            return
except ZeroDivisionError:
    print("Outer ZeroDivisionError exception caught")
