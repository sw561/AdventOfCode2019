#!/usr/bin/env python3

from solve import solve

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

with open("20_donut/test_input.txt", 'r') as f:
    s = f.read().replace(' ', '#').split()

assertEqual(solve(s), 23)

with open("20_donut/test_input2.txt", 'r') as f:
    s = f.read().replace(' ', '#').split()

assertEqual(solve(s), 58)

print("Test passed")
