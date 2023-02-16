# 98_diabolical_decorotor_generic_answer.py

class dog:
    ...

class add_cls_method:
    def __init__(self, cls):
        self.cls = cls
    def __call__(self, func):
        setattr(self.cls, func.__name__, func)

@add_cls_method(dog)
def walk():
    print("bark bark!")

print(dog.walk())