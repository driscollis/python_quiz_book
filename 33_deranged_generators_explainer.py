# 33_deranged_generators_explainer.py

array = [21, 49, 15]
gen = ((x, print(x, array)) for x in array)
array = [0, 49, 88]
print(list(gen))

for item in [21, 49, 15]:
    print(f"{array=} {item=}")
    if array.count(item) > 0:
        print(f"Item found at least once: {item=}")