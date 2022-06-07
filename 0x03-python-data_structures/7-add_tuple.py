#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = ()
    tuple_b = ()
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        return (a, 0)
    elif len(tuple_a) >= 2 or len(tuple_b) >= 2:
        return (a, b)
    return (tuple(map(lambda a, b: a + b, tuple_a, tuple_b)))
