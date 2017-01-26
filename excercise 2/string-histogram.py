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

if __name__ == "__main__":
    main()
