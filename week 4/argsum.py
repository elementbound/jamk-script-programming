# 4-2) Sum of arguments
#
# Calculate the sum of the list of command arguments

from sys import argv

def main():
    numbers = [int(x) for x in argv[1:]]
    print('Arguments: {0} \nSum: {1}'.format(argv[1:], sum(numbers)))

if __name__ == '__main__':
    main()
