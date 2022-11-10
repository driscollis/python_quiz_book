# 28_boolean_shenanigans.py

print(bool(bool((lambda a, b: a * b)(4, 5)) - bool(True)))