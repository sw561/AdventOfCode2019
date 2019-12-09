#!/usr/bin/env python3

from prog import solve

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

with open("05_program_test/input.txt", 'r') as f:
    prog = [int(x) for x in f.read().split(',')]
out = solve(prog, 1)
for j in out[:-1]:
    assertEqual(j, 0)

# tests if equal to 8
test = [3,9,8,9,10,9,4,9,99,-1,8]
assertEqual(solve(test, 8), [1])
assertEqual(solve(test, 9), [0])
assertEqual(solve(test, 0), [0])

# tests if equal to 8
test = [3,3,1108,-1,8,3,4,3,99]
assertEqual(solve(test, 8), [1])
assertEqual(solve(test, 9), [0])
assertEqual(solve(test, 0), [0])

# test if less than 8
test = [3,9,7,9,10,9,4,9,99,-1,8]
assertEqual(solve(test, 8), [0])
assertEqual(solve(test, 9), [0])
assertEqual(solve(test, 0), [1])
assertEqual(solve(test, 7), [1])

# test if less than 8
test = [3,3,1107,-1,8,3,4,3,99]
assertEqual(solve(test, 8), [0])
assertEqual(solve(test, 9), [0])
assertEqual(solve(test, 0), [1])
assertEqual(solve(test, 7), [1])

# tests if input is non-zero
test = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
assertEqual(solve(test, 8), [1])
assertEqual(solve(test, 9), [1])
assertEqual(solve(test, 0), [0])
assertEqual(solve(test, 1), [1])

# tests if input is non-zero
test = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
assertEqual(solve(test, 8), [1])
assertEqual(solve(test, 9), [1])
assertEqual(solve(test, 0), [0])
assertEqual(solve(test, 1), [1])

print("Test passed")
