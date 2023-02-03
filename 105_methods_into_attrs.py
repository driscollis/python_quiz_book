# 105_methods_into_attrs.py

class Total:

    def __init__(self):
        # private attribute
        self._amount = 10

    def amount(self):
        return self._amount