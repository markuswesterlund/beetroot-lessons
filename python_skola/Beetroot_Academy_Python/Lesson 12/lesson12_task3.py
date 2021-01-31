


class Fraction:

    def add(self, a, b):
        try:
            return a + b
        except ValueError:
            raise ValueError("That is not a valid fraction.")

    def sub(self, a, b):
        try:
            return a - b
        except ValueError:
            raise ValueError("That is not a valid fraction.")

    def mul(self, a, b):
        try:
            return a * b
        except ValueError:
            raise ValueError("That is not a valid fraction.")

    def div(self, a, b):
        try:
            return a // b
        except ZeroDivisionError:
            raise ZeroDivisionError("Can't divide by zero.")
        except ValueError:
            raise ValueError("That is not a valid fraction.")


f = Fraction()

print(f.add(1 / 4, 3 / 4))
print(f.sub(3 / 4, 1 / 2))
print(f.mul(1 / 2, 1 / 4))
print(f.div(3 / 4, 1 / 4))
