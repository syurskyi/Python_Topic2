### file: number.py

class Number:
    def __init__(self, start):                  # On Number(start)
        self.data = start
    def __sub__(self, other):                   # On instance - other
        return Number(self.data - other)        # Result is a new instance

from number import Number                   # Fetch class from module
X = Number(5)                               # Number.__init__(X, 5)
Y = X - 2                                   # Number.__sub__(X, 2)
print(Y.data)                                      # Y is new Number instance

