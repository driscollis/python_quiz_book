# 53_mixed_up_code_answer.py

def type_checker(variable):  # <-- Replace semicolon
    if isinstance(variable, (float, int)):  # <-- Change integer to int and change to tuple
        print(f"{variable} is a number")
    elif isinstance(variable, str):  # <-- Change string to str
        print(f"{variable} is a string")
    elif ...:
        print("{variable} is something else".format(variable))
    else:
        print("Default")   # Remove the break statement

if __name__ == "__main__":  # <-- Fix "_main_" to "__main__"
    type_checker(variable="Python")  # <-- Call the right function name