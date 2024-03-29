#!/usr/bin/env python3

import numpy as np
try:
    from numba import jit
except ImportError:
    # dummy decorator
    def jit(f):
        return f

@jit
def calculate_partial_sums(x, partial):
    for i in range(len(partial)-1):
        partial[i+1] = partial[i] + x[i]

def get_index_blocks(base, n, a, b):
    k = 0
    while True:
        start = (k+a)*base-1
        end = (k+b)*base-1
        if end < n:
            yield start, end
        elif start < n:
            yield start, n
            return
        else:
            return

        k += 4

def plus_indices(base, n):
    yield from get_index_blocks(base, n, 1, 2)

def minus_indices(base, n):
    yield from get_index_blocks(base, n, 3, 4)

@jit
def opt_phase(signal, partial, start, end):
    p_last = partial[-1]
    for i in range(start, end):
        signal[i] = (p_last - partial[i]) % 10

def phase(signal, partial, offset, n):

    change_algo = max(n//2 - offset, 0)

    for i in range(change_algo):
        x = 0
        for start, end in plus_indices(i+1+offset, n):
            x += partial[end-offset] - partial[start-offset]
        for start, end in minus_indices(i+1+offset, n):
            x -= partial[end-offset] - partial[start-offset]

        signal[i] = abs(x) % 10

    opt_phase(signal, partial, change_algo, n-offset)

def evolve(signal, offset=0, n=None, n_phases=100):
    if n is None:
        n = len(signal)
    partial_sums = np.zeros(n - offset + 1, dtype=int)

    for count in range(n_phases):
        calculate_partial_sums(signal, partial_sums)
        phase(signal, partial_sums, offset, n)

    return signal

def part2(signal, offset=None, rep=10000):
    # Generate new signal starting at offset given by first 7 digits of signal
    # and then from signal repeated 10000 times

    if offset is None:
        offset = int(signal[:7])

    n = len(signal)*rep

    new_signal = np.zeros(n-offset, dtype=int)

    for i in range(offset, n):
        new_signal[i-offset] = int(signal[i%len(signal)])

    return new_signal, offset, n

def main():
    with open("16_fft/input.txt", 'r') as f:
        signal = f.read().strip()

    p1 = [int(x) for x in signal]
    p1 = evolve(np.array(p1))

    print("".join(str(i) for i, x in zip(p1, range(8))))

    p2, offset, n = part2(signal)
    p2 = evolve(p2, offset, n)

    print("".join(str(i) for i, x in zip(p2, range(8))))

if __name__=="__main__":
    main()
