class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

def main():
    students = [Student('jim', 4, 19),Student('jane', 3, 22),Student('tim', 5, 20),Student('kim',1, 25),Student('ann',2, 19)]

    age_sorted = sorted(students, key=lambda x: x.age)
    grade_sorted = sorted(students, key=lambda x: x.grade)

    print('Sorted by age: \n', '\n'.join([str(x) for x in age_sorted]), '\n', sep='')
    print('Sorted by grade: \n', '\n'.join([str(x) for x in grade_sorted]), '\n', sep='')

if __name__ == '__main__':
    main()
