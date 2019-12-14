#!/usr/bin/env python3

from solve import process_input, calculate_priorities, solve

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

for fname, part1, part2 in [
        ("14_chemicals/test_input.txt", 31, None),
        ("14_chemicals/test_input1.txt", 165, None),
        ("14_chemicals/test_input2.txt", 13312, 82892753),
        ("14_chemicals/test_input3.txt", 180697, 5586022),
        ("14_chemicals/test_input4.txt", 2210736, 460664),
        ]:
    with open(fname, 'r') as f:
        reactants, products, reactions = process_input(f)

    priorities = calculate_priorities(reactants, products)
    r = solve(priorities, reactions)
    assertEqual(r, part1)

    if part2 is not None:
        p2 = solve(priorities, reactions, part2=True)
        assertEqual(p2, part2)

        n_ore = solve(priorities, reactions, n_fuel=p2)
        assert n_ore <= 1e12
        n_ore = solve(priorities, reactions, n_fuel=p2+1)
        assert n_ore > 1e12

print("Test passed")
