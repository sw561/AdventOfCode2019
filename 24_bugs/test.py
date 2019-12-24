#!/usr/bin/env python3

from solve import process, solve

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

m = """....#
#..#.
#..##
..#..
#...."""

m = process(m)

assertEqual(solve(m), 2129920)

print("Test passed")
