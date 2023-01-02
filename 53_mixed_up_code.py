# 53_mixed_up_code.py

def type_checker(variable);
    if isinstance(variable, [float, integer]):
        print(f"{variable} is a number")
    elif isinstance(variable, string):
        print(f"{variable} is a string")
    elif ...:
        print("{variable} is something else".format(variable))
    else:
        break

if __name__ == "_main_":
    typ_checker(variable="Python")