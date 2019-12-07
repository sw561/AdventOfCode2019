#!/usr/bin/env python3

from orbits import processInput, part1, route

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

children, parents = processInput("06_orbits/test_input.txt")

assertEqual(part1(children), 42)
assertEqual(route(parents, 'K', 'I'), 4)

print("Test passed")
