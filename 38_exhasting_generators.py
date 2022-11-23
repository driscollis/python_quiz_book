# 38_exhausting_genetators.py

def numbers():
    yield 1
    yield 2

if __name__ == "__main__":
    x = numbers()
    next(x)
    next(x)
    next(x)
