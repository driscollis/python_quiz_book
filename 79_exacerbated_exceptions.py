# 79_exacerbated_exceptions.py

my_list = ["Python", "Boa", "Anaconda"]
try:
    print(my_list[4])
except IndexError, ValueError:
    print("Caught an error!")
