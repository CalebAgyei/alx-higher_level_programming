#!/usr/bin/python3
"""Creates a function that reads a text file (UTF8) and prints to stdout."""


def read_file(filename=""):
    """Read text files in UTF8.

    Args:
        @filename: Name of the text file to read.
    """

    with open(filename, 'r', encoding="utf-8") as f:
        line = f.read()
        print(line)


if __name__ == "__main__":
    pass
