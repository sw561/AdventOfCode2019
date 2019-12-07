#!/usr/bin/env python3

def build_number(narr, x=None):
    if x is None:
        x = len(narr) - 1
    if x < 0:
        return 0
    return narr[x] + 10 * build_number(narr, x-1)

def solve(minima, maxima, part2=False):

    # minimum and maximum are arrays of thresholds for each pos

    def f(rep_position, rep_digit, previous_digits):

        pos = len(previous_digits)

        x = build_number(previous_digits)
        if x < minima[pos] or x > maxima[pos]:
            return

        if pos == 6:
            yield x
            return

        if pos == rep_position:
            previous_digits.append(rep_digit)
            previous_digits.append(rep_digit)
            yield from f(rep_position, rep_digit, previous_digits)
            previous_digits.pop()
            previous_digits.pop()
            return

        if pos > 0:
            last = previous_digits[-1]
        else:
            last = 0

        if pos < rep_position:
            start = last
            if not part2:
                end = rep_digit
            else:
                end = rep_digit - 1
        else:
            if not part2:
                start = max(rep_digit, last)
            else:
                start = max(rep_digit+1, last)
            end = 9

        for val in range(start, end+1):

            previous_digits.append(val)
            yield from f(rep_position, rep_digit, previous_digits)
            previous_digits.pop()

    for rep_position in range(5):
        for rep_digit in range(10):
            yield from f(rep_position, rep_digit, [])

if __name__=="__main__":

    with open("04_password/input.txt", 'r') as f:
        a, b = (x for x in f.read().strip().split('-'))

    minima = [0] + [int(a[:i+1]) for i in range(len(a))]
    maxima = [0] + [int(b[:i+1]) for i in range(len(b))]

    sols = set(solve(minima, maxima))
    print(len(sols))

    sols = set(solve(minima, maxima, part2=True))
    print(len(sols))
