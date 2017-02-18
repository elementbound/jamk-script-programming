# Exercise 5-3: Create calculator using operator module
#
# The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python.

class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(lhs, rhs):
        return Calculator(lhs.value + rhs.value)

    def __mul__(lhs, rhs):
        return Calculator(lhs.value * rhs.value)

    def __repr__(self):
        return 'Calculator({0})'.format(self.value)

def main():
    c1 = Calculator(15)
    c2 = Calculator(2)

    print('c1 + c2 = ', c1+c2)
    print('c1 * c2 = ', c1*c2)

if __name__ == '__main__':
    main()
