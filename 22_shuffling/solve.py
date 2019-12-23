#!/usr/bin/env python3

def stack(i, n):
    return n-i-1

def cut(x):
    def f(i, n):
        return (i - x) % n
    f.__name__="cut {}".format(x)
    return f

def increment(x):
    def f(i, n):
        return (i * x) % n
    f.__name__="increment {}".format(x)
    return f

def get_position(fs, i, n=10007):
    p = i
    for f in fs:
        p = f(p, n)
    return p

def process_input(lines):
    fs = []
    for line in lines:
        if line.endswith("stack"):
            fs.append(stack)
        elif line.startswith("deal with"):
            inc = int(line.split()[-1])
            fs.append(increment(inc))
        elif line.startswith("cut"):
            c = int(line.split()[-1])
            fs.append(cut(c))
    return fs

if __name__=="__main__":
    with open("22_shuffling/input.txt", 'r') as f:
        fs = process_input([line.strip() for line in f])

    print(get_position(fs, 2019))
