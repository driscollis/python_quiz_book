# 98_diabolical_decorator_alternate.py

class dog:
    ...


def enhance_dog(func):
    setattr(dog, "on_leash", func)

@enhance_dog
def walk():
    print("bark bark!")

print(dog.on_leash())