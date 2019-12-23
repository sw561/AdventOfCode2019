#!/usr/bin/env python3

from functools import reduce
from operator import mul

class ModLinearFunction:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def __mul__(self, other):
        # Function composition.
        # Return a new function f s.t. f(x) = self(other(x))
        #
        # self.a (other.a x + other.b) + self.b
        # = (self.a * other.a) * x + (self.a * other.b + self.b)
        assert self.n == other.n

        a = (self.a * other.a) % self.n
        b = (self.a * other.b + self.b) % self.n
        return ModLinearFunction(a, b, self.n)

    def __pow__(self, n):
        if n == 1:
            return self
        temp = self ** (n // 2)
        f = temp * temp
        if n % 2:
            f *= self
        return f

    def __call__(self, x):
        return (self.a * x + self.b) % self.n

    def __str__(self):
        return "({} * x + {}) % {}".format(self.a, self.b, self.n)

def stack(n):
    return ModLinearFunction(-1, n-1, n)

def cut(x, n):
    return ModLinearFunction(1, -x, n)

def increment(x, n):
    return ModLinearFunction(x, 0, n)

def inverse_increment(x, n):
    # Fermat's little theorem for p, prime:
    #
    #  a^p = a % p
    #
    #  a^(p-1) = 1 % p
    #
    #  inverse(a) = a^(p-2) % p
    #
    #  i / x = i * x^(p-2) % p
    inv_x = pow(x, n-2, n)
    return ModLinearFunction(inv_x, 0, n)

def process_input(lines, n):
    fs = []
    inv_fs = []
    for line in lines:
        if line.endswith("stack"):
            fs.append(stack(n))
            inv_fs.append(stack(n))
        elif line.startswith("deal with"):
            inc = int(line.split()[-1])
            fs.append(increment(inc, n))
            inv_fs.append(inverse_increment(inc, n))
        elif line.startswith("cut"):
            c = int(line.split()[-1])
            fs.append(cut(c, n))
            inv_fs.append(cut(-c, n))
    return fs, inv_fs

if __name__=="__main__":
    with open("22_shuffling/input.txt", 'r') as f:
        data = [line.strip() for line in f]

    # Part 1
    fs, _ = process_input(data, 10007)
    f = reduce(mul, reversed(fs))
    print(f(2019))

    # Part 2
    _, inv_fs = process_input(data, 119315717514047)
    f = reduce(mul, inv_fs)
    fn = f**101741582076661
    print(fn(2020))
