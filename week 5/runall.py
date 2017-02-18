import person
import worker
import calculator
import workersort
import student
import triangle

def header(text):
    full_length = 64
    postfix_length = full_length - 2 - len(text) - 1

    print('\n=', text, '=' * postfix_length)

def main():
    header('5-1: Person class')
    person.main()

    header('5-2: Inheritance')
    worker.main()

    header('5-3: Calculator')
    calculator.main()

    header('5-4: Worker sorting')
    workersort.main()

    header('5-5: Student sorting')
    student.main()

    header('5-6: Triangle class')
    triangle.main()

if __name__ == '__main__':
    main()
