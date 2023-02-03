# 73_indexing_indignation.py

class Number:
    integer = 0
    def __index__(self):
        internal_int = Number.integer
        Number.integer += 10
        return internal_int

print([x for x in range(Number(), Number())])