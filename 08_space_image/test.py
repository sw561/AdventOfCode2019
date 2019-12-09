#!/usr/bin/env python3

from image import get_layers, np, part2

data = np.array([int(x) for x in "123456789012"])

layers = get_layers(3, 2, data)

assert np.array_equal(layers[0], np.array([np.array([1, 2, 3]), np.array([4, 5, 6])]))
assert np.array_equal(layers[1], np.array([np.array([7, 8, 9]), np.array([0, 1, 2])]))

data = np.array([int(x) for x in "0222112222120000"])
layers = get_layers(2, 2, data)

part2(layers)

print("Test passed")
