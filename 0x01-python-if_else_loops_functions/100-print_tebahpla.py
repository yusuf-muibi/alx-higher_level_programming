#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(i - 32 if i % 2 == 1 else i), end="")
