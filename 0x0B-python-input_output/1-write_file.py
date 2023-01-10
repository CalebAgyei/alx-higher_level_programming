#!/usr/bin/python3
"""Creates a function that writes a string."""


def write_file(filename="", text=""):
    """Writes a string to a text file in UTF8.

    Args:
        @filename: Name of the text file to read.
        @text: Test to write to file.

    Return:
        Number of characters written.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        write_file = f.write(text)
        return (write_file)
