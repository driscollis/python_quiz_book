# 04_type_addition.py

my_list = [True, 1, "python", 5, False, {}, True]
integers_found = 0
bools_found = 0

for item in my_list:
    if isinstance(item, int):
        integers_found += 1
    elif isinstance(item, bool):
        bools_found += 1

print(f"{integers_found = } {bools_found = }")