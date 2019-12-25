#!/usr/bin/env python3

from solve import process, solve, solve_part2, copy

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

d = process(m)

assertEqual(solve(copy(d)), 2129920)

assertEqual(solve_part2(d, 10), 99)

print("Test passed")
