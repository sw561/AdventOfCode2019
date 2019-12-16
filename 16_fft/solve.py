#!/usr/bin/env python3

def calculate_partial_sums(x, partial, np):
    for i in range(1, np):
        partial[i] = partial[i-1] + x[i-1]

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

def phase(signal, partial, offset, n):
    for i in range(n-offset):
        if (i+offset) < (n // 2):
            x = 0
            for start, end in plus_indices(i+1+offset, n):
                x += partial[end-offset] - partial[start-offset]
            for start, end in minus_indices(i+1+offset, n):
                x -= partial[end-offset] - partial[start-offset]
        else:
            x = partial[-1] - partial[i]

        if x >= 0:
            signal[i] = x % 10
        else:
            signal[i] = -x % 10

def evolve(signal, offset=0, n=None, n_phases=100):
    if n is None:
        n = len(signal)
    partial_sums = [0]*(n - offset + 1)

    for count in range(n_phases):
        calculate_partial_sums(signal, partial_sums, n-offset+1)
        phase(signal, partial_sums, offset, n)

    return signal

def part2(signal, offset=None, rep=10000):
    # Generate new signal starting at offset given by first 7 digits of signal
    # and then from signal repeated 10000 times

    if offset is None:
        offset = int(signal[:7])

    n = len(signal)*rep

    new_signal = [0]*(n-offset)

    for i in range(offset, n):
        new_signal[i-offset] = int(signal[i%len(signal)])

    return new_signal, offset, n

def main():
    with open("16_fft/input.txt", 'r') as f:
        signal = f.read().strip()

    p1 = [int(x) for x in signal]
    evolve(p1)

    print("".join(str(i) for i, x in zip(p1, range(8))))

    p2, offset, n = part2(signal)
    evolve(p2, offset, n)

    print("".join(str(i) for i, x in zip(p2, range(8))))

if __name__=="__main__":
    main()
