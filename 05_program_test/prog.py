#!/usr/bin/env python3

from copy import copy

def decouple(code):
    # Return op-code, and parameter modes

    mode3 = code // 10000
    mode2 = code // 1000 % 10
    mode1 = code // 100  % 10
    op = code % 100

    return op, mode1, mode2, mode3

def read(prog, val, mode):
    if mode == 1:
        # immediate mode
        return val
    elif mode == 0:
        # position mode
        return prog[val]
    else:
        raise Exception("unrecognized mode")

def run(prog, my_input=None):
    p = 0
    while True:
        op, mode1, mode2, mode3 = decouple(prog[p])

        if op in [1,2,7,8]:
            a = read(prog, prog[p+1], mode1)
            b = read(prog, prog[p+2], mode2)
            ret_pointer = prog[p+3]

            if op == 1:
                prog[ret_pointer] = a + b
            elif op == 2:
                prog[ret_pointer] = a * b
            elif op == 7:
                prog[ret_pointer] = int(a < b)
            elif op == 8:
                prog[ret_pointer] = int(a == b)
            else:
                raise Exception("HELP: op = {} not handled".format(op))
            p += 4

        elif op == 3:
            if my_input is None:
                prog[prog[p+1]] = int(input("Please input\n"))
            else:
                prog[prog[p+1]] = next(my_input)
            p += 2

        elif op == 4:
            a = read(prog, prog[p+1], mode1)
            yield a
            p += 2

        elif op in [5, 6]:
            a = read(prog, prog[p+1], mode1)
            b = read(prog, prog[p+2], mode2)
            if (op==5 and a) or (op==6 and not a):
                p = b
            else:
                p += 3

        elif op == 99:
            break

        else:
            raise Exception("Unrecognized op code: {}".format(op))

def solve(prog, ID):
    def input_g():
        yield ID

    out = list(run(prog, my_input=input_g()))
    return out

if __name__=="__main__":
    with open("05_program_test/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    out = solve(copy(prog), 1)
    print(out[-1])
    out = solve(prog, 5)
    print(out[-1])