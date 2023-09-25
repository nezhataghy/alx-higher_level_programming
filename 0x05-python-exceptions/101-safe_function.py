#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
    except Exception as error:
        stderr.write("Exception: {}\n".format(error))
        result = None

    return (result)
