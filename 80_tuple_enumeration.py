# 80_tuple_enumeration.py

# Which of the following is the correct way to enumerate the tuple?

list_of_tuples = [("snake", "Python"), ("rodent", "hamster")]

# A)
for i, genus, animal in enumerate(list_of_tuples):
    print(f"{i} {genus = } {animal =}")

# B)
for i, (genus, animal) in enumerate(list_of_tuples):
    print(f"{i} {genus = } {animal =}")

# C)
for genus, animal in enumerate(list_of_tuples):
    print(f"{i} {genus = } {animal =}")

