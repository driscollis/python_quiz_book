# 33_deranged_generators.py

array = [21, 49, 15]
gen = (x for x in array if array.count(x) > 0)
array = [0, 49, 88]
print(list(gen))