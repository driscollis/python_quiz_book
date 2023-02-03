# 105_methods_into_attrs_answer.py

class Total:

    def __init__(self):
        # private attribute
        self._amount = 10

    @property
    def amount(self):
        return self._amount