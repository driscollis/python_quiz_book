# 60_subclassing_silliness.py

class MyClass(str):
    pass


silly_dict = {"py": "amazing"}
p = MyClass("py")
silly_dict[p] = 10
print(silly_dict)