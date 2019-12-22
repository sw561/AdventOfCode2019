#!/usr/bin/env python3

import sys
sys.path.append('.')
from intcode_computer import ProgramInstance

def gen_from_input(my_f, verbose=True):
    if my_f is None:
        while True:
            yield input()
    else:
        with open(my_f, 'r') as f:
            for line in f:
                l = line.strip()
                if l.startswith('#') or l.startswith('//'):
                    continue
                if verbose:
                    print(line.strip())
                yield line.strip()

def simulate(prog, my_f, verbose=True):
    p = ProgramInstance(prog)
    my_prog = gen_from_input(my_f, verbose)

    while p.status != "EXIT":
        s = next(my_prog)
        s = [ord(i.upper()) for i in s] + [ord('\n')]
        # print("About to start inputting instruction", s)
        for x in s:
            out = p.run(x)
            for i in out:
                if verbose:
                    print(chr(i) if i < 128 else i, end='')
                else:
                    if i >= 128:
                        print(i)

def main():
    with open("21_springdroid/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    if len(sys.argv) >= 2:
        simulate(prog, sys.argv[1])
    else:
        simulate(prog, "21_springdroid/part1.springscript", verbose=False)
        simulate(prog, "21_springdroid/part2.springscript", verbose=False)

if __name__=="__main__":
    main()
