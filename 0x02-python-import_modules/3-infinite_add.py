#!/usr/bin/python3
if __name__ == '__main__':
    """Prints the sum up interger passed and print"""
    import sys

    result = 0
    count = len(sys.argv) - 1
    for i in range(count):
        num = int(sys.argv[i + 1])
        result = result + num
    print(result)
