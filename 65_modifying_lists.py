# 65_modifying_lists.py

animals = {1: "Python"}
loops = 1
for key in animals:
    del animals[key]
    animals[key + 1] = None
    print(f"{loops = }")
    loops += 1