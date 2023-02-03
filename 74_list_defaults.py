# 74_list_defaults.py

def my_function(default=[]):
    default.append("Python")
    return default

my_function()
print(my_function())
