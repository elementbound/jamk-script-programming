# 2-1) calculate characters in a string
#
# Give a string and search how many 'a/A' or 'e/E' letters there are in the string
# How to count all letters in a string?

from string import ascii_letters

def main():
    # Init dictionary with letters
    histogram = {}

    for c in ascii_letters:
        histogram[c] = 0

    # Input string and histogram it
    text = input()

    for c in text:
        if c in histogram:
            histogram[c] += 1

    # Display
    print('a/A:', histogram['a']+histogram['A'])
    print('e/E:', histogram['e']+histogram['E'])

def main_short():
    text = input().lower()
    print('a/A', text.count('a'))
    print('e/E', text.count('e'))

if __name__ == "__main__":
    main_short()
