#!/usr/bin/env python3

def MyArray(start, end):
    return [[0]*(end-start), start, end]

def calculate_partial_sums(s0, p0):
    # p0 = partial_sums[0]
    # s0 = signal[0]
    for i in range(1, len(p0)):
        p0[i] = p0[i-1] + s0[i-1]

def plus_indices(base, n):
    k = 0
    while True:
        start = (k+1)*base-1
        end = (k+2)*base-1
        if end < n:
            yield start, end
        elif start < n:
            yield start, n
            return
        else:
            return

        k += 4

def minus_indices(base, n):
    k = 0
    while True:
        start = (k+3)*base-1
        end = (k+4)*base-1
        if end < n:
            yield start, end
        elif start < n:
            yield start, n
            return
        else:
            return

        k += 4

def phase(s0, p0, offset, n):
    for i in range(offset, n):
        if i < (n // 2):
            x = 0
            for start, end in plus_indices(i+1, n):
                x += p0[end-offset] - p0[start-offset]
            for start, end in minus_indices(i+1, n):
                x -= p0[end-offset] - p0[start-offset]
        else:
            x = p0[n-offset] - p0[i-offset]

        if x >= 0:
            s0[i-offset] = x % 10
        else:
            s0[i-offset] = -x % 10

def evolve(signal, n):
    partial_sums = MyArray(signal[1], signal[2]+1)

    for count in range(n):
        calculate_partial_sums(signal[0], partial_sums[0])
        phase(signal[0], partial_sums[0], signal[1], signal[2])

    return signal

def part1(signal):
    new_signal = MyArray(0, len(signal))
    for i in range(new_signal[1], new_signal[2]):
        new_signal[0][i-new_signal[1]] = int(signal[i])

    return new_signal

def part2(signal, offset=None, rep=10000):
    # Generate new signal starting at offset given by first 7 digits of signal
    # and then from signal repeated 10000 times

    if offset is None:
        offset = int(signal[:7])

    new_signal = MyArray(start=offset, end=len(signal)*rep)

    for i in range(new_signal[1], new_signal[2]):
        new_signal[0][i-new_signal[1]] = int(signal[i%len(signal)])

    return new_signal

if __name__=="__main__":
    with open("16_fft/input.txt", 'r') as f:
        signal = f.read().strip()

    p1 = part1(signal)
    evolve(p1, 100)

    print("".join(str(i) for i, x in zip(p1[0], range(8))))

    p2 = part2(signal)
    evolve(p2, 100)

    print("".join(str(i) for i, x in zip(p2[0], range(8))))
