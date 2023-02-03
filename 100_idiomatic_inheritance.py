# 100_idiomatic_inheritance.py

class Py:
    py = 1

class Cy(Py):
    ...

class Vy(Py):
    ...

Cy.py = 3.14
Py.py = 7
print(f"{Py.py = } {Cy.py = } {Vy.py = }")