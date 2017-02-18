# Exercise 5-6: Triangle class
#
# Plan, create and test a class called Triangle.
#
# * calculate the Area of Triangle with two different way
# * calculate also the total perimeter of the Triangle

import math

class Triangle:
    def __init__(self, a, b, c):
        # Init sides
        self.sides = [a, b, c]

        # Init angles
        alpha = math.acos((-a*a + b*b + c*c) / (2*b*c))
        beta  = math.acos(( a*a - b*b + c*c) / (2*a*c))
        gamma = math.acos(( a*a + b*b - c*c) / (2*a*b))
        self.angles = [alpha, beta, gamma]

    def perimeter(self):
        return sum(self.sides)

    def area_heron(self):
        s = self.perimeter()/2
        (a, b, c) = self.sides

        return math.sqrt(s*(s-a)*(s-b)*(s-c))

    def area_bh(self):
        base = self.sides[2]
        height = math.sin(self.angles[0]) * self.sides[1]

        return 0.5 * base * height

def main():
    triangle = Triangle(203, 145, 208)
    print('Sides:', triangle.sides)
    print('Angles:', [math.degrees(x) for x in triangle.angles])
    print('Perimeter: ', triangle.perimeter())
    print('Area (Heron\'s formula):', triangle.area_heron())
    print('Area (base-height):', triangle.area_bh())

if __name__ == "__main__":
    main()
