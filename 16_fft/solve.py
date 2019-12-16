#!/usr/bin/env python3

def calculate_partial_sums(signal, partial_sums):
    for i in range(1, len(signal)+1):
        partial_sums[i] = partial_sums[i-1] + signal[i-1]

def plus_indices(base, n):
    k = 0
    while True:
        start = (k+1)*base-1
        end = (k+2)*base-1
        if start >= n:
            return
        elif end >= n:
            yield start, n
            return
        else:
            yield start, end

        k += 4

def minus_indices(base, n):
    k = 0
    while True:
        start = (k+3)*base-1
        end = (k+4)*base-1
        if start >= n:
            return
        elif end >= n:
            yield start, n
            return
        else:
            yield start, end

        k += 4

def phase(new_signal, partial_sums):
    n = len(new_signal)
    for i in range(n):
        new_signal[i] = abs(
            sum(partial_sums[end] - partial_sums[start] for start, end in plus_indices(i+1, n)) -
            sum(partial_sums[end] - partial_sums[start] for start, end in minus_indices(i+1, n))
            ) % 10

def evolve(signal, n):
    new_signal = [0] * len(signal)
    partial_sums = [0] * (len(signal) + 1)

    for _ in range(n):
        calculate_partial_sums(signal, partial_sums)
        phase(new_signal, partial_sums)
        signal, new_signal = new_signal, signal

    return signal

if __name__=="__main__":
    with open("16_fft/input.txt", 'r') as f:
        signal = [int(x) for x in f.read().strip()]

    evolve(signal, 100)

    print("".join(map(str, signal[:8])))
