#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        f = fct(*args)
        return (f)
    except BaseException as err:
        print("BaseException: {}".format(err), file=sys.stderr)
        return None
