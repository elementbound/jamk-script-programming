# 2-2) Byte, Kilobyte, Megabyte, Gigabyte converter
#
# Insert bytes and then your program shows many bytes in a kilobyte, megabyte and gigabyte.
# You must real mega, giga and tera definations (so for example 2^20 or 2^30)
# background information http://www.whatsabyte.com/

def main():
    # Define units and their postifxes
    units = ['Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes']
    postfixes = ['B', 'KB', 'MB', 'GB']

    # Get input value; make sure it's a number
    while True:
        try:
            size = input('Give your input in bytes: ')
            size = int(size)
            break
        except ValueError:
            print('Not a number!')

    # Display sizes
    for unit, postfix in zip(units, postfixes):
        print('{0: <16} {1: <16} {2}'.format(unit, size, postfix))
        size /= 1024

if __name__ == "__main__":
    main()
