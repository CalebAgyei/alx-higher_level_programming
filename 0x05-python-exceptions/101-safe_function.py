#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct()
    except Exception as exc:
        return None
        sys.stderr.write("Exception:", exc.args)
    else:
        return fct
