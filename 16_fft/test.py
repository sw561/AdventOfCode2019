#!/usr/bin/env python3

from solve import phase, evolve

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

signal = [int(x) for x in "12345678"]

signal = evolve(signal, 4)
for s1, s2 in zip(signal, [int(x) for x in "01029498"]):
    assertEqual(s1, s2)

tests = [
("80871224585914546619083218645595", "24176176"),
("19617804207202209144916044189917", "73745418"),
("69317163492948606335995924319873", "52432133"),
]

for signal, out in tests:
    signal = [int(x) for x in signal]

    evolve(signal, 100)

    print("".join(map(str, signal)))

    for s1, s2 in zip(signal, out):
        assertEqual(s1, int(s2))

print("Test passed")
