# 2-5) multiplication table
#
# Calculate the multiplication table
# based on the upper limit given by the user

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
    limit = int_input('Upper limit> ')

    for i in range(1, limit+1):
        for j in range(1, limit+1):
            print('{0} * {1} = {2}'.format(i,j,i*j))
        print('')

if __name__ == "__main__":
    main()
