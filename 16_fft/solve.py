#!/usr/bin/env python3

class MyArray(list):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.data = [0]*(end-start)

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return self.data[i - self.start]

    def __setitem__(self, i, x):
        self.data[i - self.start] = x

def calculate_partial_sums(signal, partial_sums):
    for i in range(partial_sums.start+1, partial_sums.end):
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

def phase(signal, partial_sums):
    for i in range(signal.start, signal.end):
        signal[i] = abs(
            sum(partial_sums[end] - partial_sums[start] for start, end in plus_indices(i+1, signal.end)) -
            sum(partial_sums[end] - partial_sums[start] for start, end in minus_indices(i+1, signal.end))
            ) % 10

def evolve(signal, n):
    partial_sums = MyArray(signal.start, signal.end+1)

    for count in range(n):
        calculate_partial_sums(signal, partial_sums)
        phase(signal, partial_sums)

    return signal

def part1(signal):
    new_signal = MyArray(0, len(signal))
    for i in range(new_signal.start, new_signal.end):
        new_signal[i] = int(signal[i])

    return new_signal

def part2(signal):
    # Generate new signal starting at offset given by first 7 digits of signal
    # and then from signal repeated 10000 times

    offset = int(signal[:7])

    new_signal = MyArray(start=offset, end=len(signal)*10000)

    for i in range(new_signal.start, new_signal.end):
        new_signal[i] = int(signal[i%len(signal)])

    return new_signal

if __name__=="__main__":
    with open("16_fft/input.txt", 'r') as f:
        signal = f.read().strip()

    p1 = part1(signal)
    evolve(p1, 100)

    print("".join(str(i) for i, x in zip(p1, range(8))))

    p2 = part2(signal)
    evolve(p2, 100)

    print("".join(str(i) for i, x in zip(p2, range(8))))
