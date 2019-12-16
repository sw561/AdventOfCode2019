#!/usr/bin/env python3

from solve import phase, evolve, MyArray, part1, part2

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

signal = part1("12345678")

signal = evolve(signal, 4)
for s1, s2 in zip(signal[0], [int(x) for x in "01029498"]):
    assertEqual(s1, s2)

tests = [
("80871224585914546619083218645595", "24176176"),
("19617804207202209144916044189917", "73745418"),
("69317163492948606335995924319873", "52432133"),
]

for signal, out in tests:
    signal = part1(signal)

    evolve(signal, 100)

    print("".join(map(str, signal[0])))

    for s1, s2 in zip(signal[0], out):
        assertEqual(s1, int(s2))

offset = 20
for signal, out in tests:
    signal = part2(signal, offset=offset, rep=1)

    evolve(signal, 100)

    print(" "*offset + "".join(map(str, signal[0])))

# For part 2
tests = [
("03036732577212944063491565474664", "84462026"),
("02935109699940807407585447034323", "78725270"),
("03081770884921959731165446850517", "53553731"),
]

for signal, out in tests:
    signal = part2(signal)
    evolve(signal, 100)

    print("".join(str(i) for i, x in zip(signal[0], range(8))))

    for s1, s2 in zip(signal[0], out):
        assertEqual(s1, int(s2))

print("Test passed")
