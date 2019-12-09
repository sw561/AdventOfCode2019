#!/usr/bin/env python3

from prog import ProgramInstance

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

prog = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

p = ProgramInstance(prog)
o = p.run()
for oi, progi in zip(o, prog):
    assertEqual(oi, progi)

prog = [1102,34915192,34915192,7,4,7,99,0]
p = ProgramInstance(prog)
o = p.run()
assertEqual(len(str(o[0])), 16)

prog = [104,1125899906842624,99]
p = ProgramInstance(prog)
o = p.run()
assertEqual(o[0], 1125899906842624)

print("Test passed")
