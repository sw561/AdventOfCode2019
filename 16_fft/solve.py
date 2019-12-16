#!/usr/bin/env python3

def plus_indices(base, n):
    k = 0
    while True:
        for i in range((k+1)*base-1, (k+2)*base-1):
            if i >= n:
                return
            yield i

        k += 4

def minus_indices(base, n):
    k = 0
    while True:
        for i in range((k+3)*base-1, (k+4)*base-1):
            if i >= n:
                return
            yield i

        k += 4

def phase(signal, new_signal):
    n = len(signal)
    for i in range(n):
        new_signal[i] = abs(
            sum(signal[j] for j in plus_indices(i+1, n)) -
            sum(signal[j] for j in minus_indices(i+1, n))
            ) % 10

def evolve(signal, n):
    new_signal = [0] * len(signal)

    for _ in range(n):
        phase(signal, new_signal)
        signal, new_signal = new_signal, signal

    return signal

if __name__=="__main__":
    with open("16_fft/input.txt", 'r') as f:
        signal = [int(x) for x in f.read().strip()]

    evolve(signal, 100)

    print("".join(map(str, signal[:8])))
