#!/usr/bin/env python3

from wires import solve

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

a = "R8,U5,L5,D3".split(',')
b = "U7,R6,D4,L4".split(',')
manhattan, delay = solve(a, b)
assertEqual(manhattan, 6)
assertEqual(delay, 30)

print("Test passed")
