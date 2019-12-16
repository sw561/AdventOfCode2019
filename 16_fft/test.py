#!/usr/bin/env python3

from solve import evolve, part2, np

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

signal = np.array([int(x) for x in "12345678"])

signal = evolve(signal, n_phases=4)
for s1, s2 in zip(signal, [int(x) for x in "01029498"]):
    assertEqual(s1, s2)

tests = [
("80871224585914546619083218645595", "24176176"),
("19617804207202209144916044189917", "73745418"),
("69317163492948606335995924319873", "52432133"),
]

test_out = []

for signal, out in tests:
    signal = np.array([int(x) for x in signal])

    signal = evolve(signal)

    test_out.append("".join(map(str, signal)))
    # print("".join(map(str, signal)))

    for s1, s2 in zip(signal, out):
        assertEqual(s1, int(s2))

offset = 20
for (signal, out), to in zip(tests, test_out):
    signal, offset, n = part2(signal, offset=offset, rep=1)

    signal = evolve(signal, offset, n)

    # print(" "*offset + "".join(map(str, signal)))
    s = "".join(map(str, signal))
    assert to.endswith(s)

# For part 2
tests = [
("03036732577212944063491565474664", "84462026"),
("02935109699940807407585447034323", "78725270"),
("03081770884921959731165446850517", "53553731"),
]

for signal, out in tests:
    signal, offset, n = part2(signal)
    signal = evolve(signal, offset, n)

    # print("".join(str(i) for i, x in zip(signal, range(8))))

    for s1, s2 in zip(signal, out):
        assertEqual(s1, int(s2))

print("Test passed")
