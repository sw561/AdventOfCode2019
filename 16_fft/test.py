#!/usr/bin/env python3

from solve import phase, evolve, MyArray, part2

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

signal = [int(x) for x in "12345678"]
new_signal = MyArray(0, len(signal))
for i in range(new_signal.start, new_signal.end):
    new_signal[i] = signal[i]
signal = new_signal

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
    new_signal = MyArray(0, len(signal))
    for i in range(new_signal.start, new_signal.end):
        new_signal[i] = signal[i]

    signal = new_signal

    evolve(signal, 100)

    print("".join(map(str, signal)))

    for s1, s2 in zip(signal, out):
        assertEqual(s1, int(s2))

offset = 20

for signal, out in tests:
    signal = [int(x) for x in signal]
    new_signal = MyArray(offset, len(signal))
    for i in range(new_signal.start, new_signal.end):
        new_signal[i] = signal[i]

    signal = new_signal

    evolve(signal, 100)

    print(" "*offset + "".join(map(str, signal)))

# for signal, out in tests:
#     part2(signal, offset=10)
#     print("".join(map(str, signal)))


# For part 2
tests = [
("03036732577212944063491565474664", "84462026"),
("02935109699940807407585447034323", "78725270"),
("03081770884921959731165446850517", "53553731"),
]

for signal, out in tests:
    signal = part2(signal)
    evolve(signal, 100)

    print("".join(str(i) for i, x in zip(signal, range(8))))

    for s1, s2 in zip(signal, out):
        assertEqual(s1, int(s2))

print("Test passed")
