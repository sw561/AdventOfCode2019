#!/usr/bin/env python3

from prog import simulate, solve

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

prog = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

x = simulate(prog, (4,3,2,1,0))
assertEqual(x, 43210)

x = solve(prog)
assertEqual(x, 43210)

prog = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0]

assertEqual(solve(prog), 54321)

prog = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

assertEqual(solve(prog), 65210)

print("Test passed")
