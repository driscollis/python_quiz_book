# 56_the_scope_of_the_matter.py

number = 8

def adder(integer):
    print(number)
    number = 10
    print(number + integer)

adder(5)