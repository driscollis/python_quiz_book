# 39_list_o_functions.py

functions = []

for number in range(8):
    def my_function():
        return number
    functions.append(my_function)

results = [function() for function in functions]
print(results)