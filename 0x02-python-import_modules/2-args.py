#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv_len = len(sys.argv) - 1

    if argv_len == 0:
        print("0 arguments.")
    elif argv_len == 1:
        print("1 argument:")
    else:
        print(f"{argv_len} arguments:")

    for i in range(1, argv_len + 1):
        print(f"{i}: {sys.argv[i]}")
