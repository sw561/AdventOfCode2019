#!/usr/bin/env python3

from fuel import fuel, fuel_part2

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

# Part 1
data = [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
]

for x, y in data:
    assertEqual(fuel(x), y)

# Part 2
data = [
    (14, 2),
    (1969, 966),
    (100756, 50346),
]

for x, y in data:
    assertEqual(fuel_part2(x), y)

print("Test passed")
