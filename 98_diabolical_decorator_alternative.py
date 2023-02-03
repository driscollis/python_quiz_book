# 98_diabolical_decorator_alternate.py

class dog:
    ...
    
    
def set_attr(func):
    setattr(dog, "on_leash", func)
    
def walk():
    print("bark bark!")
    
walk = set_attr(walk)    
print(dog.on_leash())