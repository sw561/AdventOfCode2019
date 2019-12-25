#!/usr/bin/env python3

import sys
sys.path.append('.')
from intcode_computer import ProgramInstance
from shutil import copyfile

def gen_from_input(my_f):
    if my_f is None:
        while True:
            yield input()
    else:
        with open(my_f, 'r') as f:
            for line in f:
                l = line.strip()
                if l.startswith('#') or l.startswith('//'):
                    continue
                print(line.strip())
                yield line.strip()

        if INTERACTIVE:
            with open(my_f, 'a') as f:
                for x in gen_from_input(None):
                    f.write(x + "\n")
                    yield x

def simulate(prog, my_f):
    p = ProgramInstance(prog)
    my_prog = gen_from_input(my_f)
    out = p.run()
    for i in out:
        print(chr(i) if i < 128 else i, end='')

    while p.status != "EXIT":

        try:
            s = next(my_prog)
        except StopIteration:
            break
        s = [ord(i) for i in s] + [ord('\n')]

        for x in s:
            out = p.run(x)

        for i in out:
            print(chr(i) if i < 128 else i, end='')

    else:
        exit("Reached exit status")

objects = [
"hypercube",
"shell",
"whirled peas",
"spool of cat6",
"mouse",
"antenna",
"hologram",
"semiconductor",
]

def systematic_try(prog):
    for i in range(256):
        copyfile("25_game/solution", "25_game/attempt")

        with open("25_game/attempt", 'a') as f:

            for j, o in enumerate(objects):
                if i & (1 << j):
                    f.write("drop {}\n".format(o))
            f.write("south\n")

        simulate(prog, "25_game/attempt")

if __name__=="__main__":
    with open("25_game/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    if len(sys.argv) >= 2:
        INTERACTIVE = True
        simulate(prog, sys.argv[1])
    else:
        INTERACTIVE = False
        systematic_try(prog)
