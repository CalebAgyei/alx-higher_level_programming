#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as exc:
        print(exc.args)
        print("Exception:", exc.args)
    else:
        return True
