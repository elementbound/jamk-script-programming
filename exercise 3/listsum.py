# 4-3) list calculation with type detection
#
# calculate sum and average of elements in the list
# ignore all values in the list that are not numbers
#
# initializing the list with the following values
#
# list = [1,2,3,4,5,6,7,8,9,20,30, "aa", "bee", 11, "test", 51, 63]

def is_int(val):
    try:
        val = int(val)
        return True
    except ValueError:
        return False

def main():
    # Initialize list
    values = [1,2,3,4,5,6,7,8,9,20,30, "aa", "bee", 11, "test", 51, 63]

    # Throw out non-integer values
    values = [x for x in values if is_int(x)]

    # Display results
    print('Sum {0}/{1} and average {2}'.format(sum(values), len(values), sum(values)/len(values))) 

if __name__ == '__main__':
    main()
