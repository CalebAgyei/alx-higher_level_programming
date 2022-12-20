#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as exc:
        return False
        sys.stderr.write("Exception:", exc.args)
    else:
        return True
