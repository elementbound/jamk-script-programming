from sys import argv

def main():
    sum = 0

    for val in argv[1:]:
        try:
            val = int(val)
            sum += val
        except ValueError:
            print(val, 'not a number, ignoring')

    print(sum)

if __name__ == "__main__":
    main()
