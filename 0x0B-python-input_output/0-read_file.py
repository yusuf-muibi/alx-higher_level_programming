#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
