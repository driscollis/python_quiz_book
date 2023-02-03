# 92_class_attributes.py

letters = ["a"]

class L:
    letters = ["b"]
    letters = letters + ["c"]
    
print(letters[0], L.letters)