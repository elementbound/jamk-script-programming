# Exercise 5-1: Person class
#
# Create an Person class with a method to check if a person is equal than
# another one.

class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(lhs, rhs):
        return lhs.name == rhs.name

if __name__ == "__main__":
    # Test with asserts 
    bill = Person("Bill")
    joe = Person("Joe")
    also_bill = Person("Bill")

    assert bill != joe
    assert bill == also_bill
