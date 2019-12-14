#!/usr/bin/env python3

from solve import process_input, calculate_priorities, solve

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

for fname, part1 in [
        ("14_chemicals/test_input.txt", 31),
        ("14_chemicals/test_input1.txt", 165)]:
    with open(fname, 'r') as f:
        reactants, products, reactions = process_input(f)

    priorities = calculate_priorities(reactants, products)
    r = solve(priorities, reactions)
    assertEqual(r, part1)
    print("--")

print("Test passed")
