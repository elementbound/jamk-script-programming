# 4-1) Count all letters in a string
#
# How to count all letters with ignore-case in a string?

from string import ascii_letters

def main():
    # Init dictionary with letters
    histogram = {}

    # Input string and histogram it
    text = input()

    for c in text.lower():
        if c not in ascii_letters:
            continue

        try:
            histogram[c] += 1
        except KeyError:
            histogram[c] = 1

    # Display results
    for letter, count in sorted(histogram.items()):
        print('{0}: {1: >4}'.format(letter, count))

if __name__ == '__main__':
    main()
