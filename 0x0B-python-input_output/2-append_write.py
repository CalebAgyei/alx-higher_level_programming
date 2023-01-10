#!/usr/bin/python3
"""Creates a function that appends a string."""


def append_write(filename="", text=""):
    """Appends a string at then end of a text file in UTF8.

    Args:
        @filename: Name of the text file to append string to.
        @text: String to append.

    Return:
        Number of characters added.
    """

    with open(filename, 'a', encoding="utf-8") as f:
        write_file = f.write(text)
        return (write_file)
