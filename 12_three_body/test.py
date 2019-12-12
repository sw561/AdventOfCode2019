#!/usr/bin/env python3

from solve import process_input, solve

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

with open("12_three_body/test_input.txt", 'r') as f:
    positions = process_input(f)

part1, part2 = solve(positions, 10)
assertEqual(part1, 179)
assertEqual(part2, 2772)

with open("12_three_body/test_input2.txt", 'r') as f:
    positions = process_input(f)

part1, part2 = solve(positions, 100)
assertEqual(part1, 1940)
assertEqual(part2, 4686774924)

print("Test passed")
