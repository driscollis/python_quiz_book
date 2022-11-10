# 05_positional_arguments.py

def positional(name, age, /, a, b, *, key):
    print(name, age, a, b, key)

if __name__ == "__main__":
    positional('Mike', 17, key='test')