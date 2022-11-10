# 04_raising_exceptions.py

try:
    for i in range(5):
        try:
            1 / 0
        except ZeroDivisionError:
            raise ZeroDivisionError("Error: You divided by zero!")
        finally:
            print("finally executed")
            break
except ZeroDivisionError:
    print("Outer ZeroDivisionError exception caught")
