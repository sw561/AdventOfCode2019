#!/usr/bin/env python3

from solve import process_input, solve

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

with open("20_donut/test_input.txt", 'r') as f:
    s = f.read().replace(' ', '#').split()

label_pos, edges = process_input(s)
assertEqual(solve(label_pos, edges), 23)
assertEqual(solve(label_pos, edges, part2=True), 26)

with open("20_donut/test_input2.txt", 'r') as f:
    s = f.read().replace(' ', '#').split()

label_pos, edges = process_input(s)
assertEqual(solve(label_pos, edges), 58)

with open("20_donut/test_input3.txt", 'r') as f:
    s = f.read().replace(' ', '#').split()

label_pos, edges = process_input(s)
assertEqual(solve(label_pos, edges, part2=True), 396)

print("Test passed")
