# 2-3) Grade calculator
#
# Ask two grades from the user:
# a) exam point   (0-24)
# b) demo points  (0-12)
# and calculate the total based on the following table:
#
# 	>= 33 	=> 5
# 	>= 29 	=> 4
# 	>= 25 	=> 3
# 	>= 21 	=> 2
# 	>= 18 	=> 1
# 	< 18   	=> 0

# Ask for an integer input
# Retry if the value can't be parsed, or ( optionally ) if value is not in range
def int_input(text='', error_text='Not a number!', range=None, range_error_text='Value out of range!'):
    while True:
        try:
            val = input(text)
            val = int(val)

            if range is not None:
                if val not in range:
                    print('{0} ({1}-{2})'.format(range_error_text, range[0], range[-1]))
                    continue

            return val
        except ValueError:
            print(error_text)

def main():
    # Define grading system
    grading = {
        5: 33,
        4: 29,
        3: 25,
        2: 21,
        1: 18,
        0: -1
    }

    # Input points from user; make sure they are numbers and they are in the right range
    exam_points = int_input('How many exam points did you get (0-24)? ', range=range(0,24+1))
    demo_points = int_input('How many demo points did you get (0-12)? ', range=range(0,12+1))
    points = exam_points + demo_points

    # Find grade
    grade = 0
    for potential_grade, required_points in sorted(grading.items())[::-1]:
        if points >= required_points:
            grade = potential_grade
            break

    print('With', points, 'points, the final grade was', grade)

if __name__ == "__main__":
    main()
