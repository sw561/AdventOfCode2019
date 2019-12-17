#!/usr/bin/env python3

from solve import alignment_parameters, my_prog_to_ascii_in

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

s = """..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^.."""

assertEqual(sum(alignment_parameters(s)), 76)

s = """A,B,C,B,A,C
R,8,R,8
R,4,R,4,R,8
L,6,L,2
y
"""

print(list(my_prog_to_ascii_in(s)))

print("Test passed")
