#!/usr/bin/env python3

from prog import ProgramInstance

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

prog = [1,1,1,4,99,5,6,0,99]

p = ProgramInstance(prog)
p.run()

final_prog = [30,1,1,4,2,5,6,0,99]

for pi, pj in zip(p.prog, final_prog):
    assertEqual(pi, pj)

print("Test passed")
