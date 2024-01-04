#!/usr/bin/python3
from add_0 import add

def main():
    """This prints the sum of 1 and 2"""
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    main()
