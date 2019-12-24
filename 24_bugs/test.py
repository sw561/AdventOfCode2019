#!/usr/bin/env python3

from solve import process, solve, solve_part2

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

assertEqual(solve_part2(m, 10), 99)

print("Test passed")
