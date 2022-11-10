# 07_list_popping.py

my_list = list(range(1, 7))
for index, item in enumerate(my_list): my_list.pop(index)
print(my_list)