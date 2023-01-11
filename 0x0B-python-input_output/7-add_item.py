#!/usr/bin/python3
"""Script that adds all arguments to a Python list, and save them to a file."""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    from sys import argv

    filename = "add_item.json"

    obj = []

    if len(argv) == 1:
        save_to_json_file(obj, filename)

    elif len(argv) >= 2:
        for i in range(1, len(argv)):
            obj.append(str(argv[i]))

            save_to_json_file(obj, filename)
