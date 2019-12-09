#!/usr/bin/env python3

from copy import copy

def decouple(code):
    # Return op-code, and parameter modes

    mode3 = code // 10000
    mode2 = code // 1000 % 10
    mode1 = code // 100  % 10
    op = code % 100

    return op, mode1, mode2, mode3

def read(prog, relative_base, val, mode):
    if mode == 1:
        # immediate mode
        return val
    elif mode == 0:
        # position mode
        return prog[val]
    elif mode == 2:
        # relative mode
        return prog[val + relative_base]
    else:
        raise Exception("unrecognized mode")

def read_pointer(relative_base, val, mode):
    if mode == 0:
        return val
    elif mode == 2:
        return relative_base + val
    else:
        raise Exception("Expecting a pointer here")

def run(prog, p=0, relative_base=0, inp=None):
    while True:
        op, mode1, mode2, mode3 = decouple(prog[p])

        if op in [1,2,7,8]:
            a = read(prog, relative_base, prog[p+1], mode1)
            b = read(prog, relative_base, prog[p+2], mode2)
            ret_pointer = read_pointer(relative_base, prog[p+3], mode3)

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
            if inp == None:
                # Need to wait for input
                return 'WAIT', (prog, p, relative_base), None
            else:
                write_pointer = read_pointer(relative_base, prog[p+1], mode1)
                prog[write_pointer] = inp
                inp = None
            p += 2

        elif op == 4:
            a = read(prog, relative_base, prog[p+1], mode1)
            p += 2
            return 'OUT', (prog, p, relative_base), a

        elif op in [5, 6]:
            a = read(prog, relative_base, prog[p+1], mode1)
            b = read(prog, relative_base, prog[p+2], mode2)
            if (op==5 and a) or (op==6 and not a):
                p = b
            else:
                p += 3

        elif op == 9:
            a = read(prog, relative_base, prog[p+1], mode1)
            relative_base += a
            p += 2

        elif op == 99:
            return 'EXIT', (None, None, None), None

        else:
            raise Exception("Unrecognized op code: {}".format(op))

class ProgramInstance:
    def __init__(self, prog):
        self.prog = copy(prog)
        self.p = 0
        self.relative_base = 0
        self.status = 'READY'

    def run(self, inp=None):
        # Run until requires input or exits, returns any output values produced
        out = []

        assert (self.status == 'READY') or (self.status == 'WAIT' and inp is not None)

        while True:
            try:
                self.status, (self.prog, self.p, self.relative_base), o = \
                        run(self.prog, self.p, self.relative_base, inp)
            except IndexError:
                if len(self.prog) < 10000:
                    self.prog = self.prog + [0] * len(self.prog)
                    # print("Expanding memory. New size = {}".format(len(self.prog)))
                    continue
                else:
                    raise
            inp = None

            if self.status == 'OUT':
                out.append(o)

            if self.status in ['WAIT', 'EXIT']:
                return out

    def __str__(self):
        return self.status

if __name__=="__main__":
    with open("09_boost/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    # Run in test mode - part 1
    p = ProgramInstance(prog)
    o = p.run(1)
    assert len(o) == 1
    print(o[0])

    # Part 2
    p = ProgramInstance(prog)
    o = p.run(2)
    assert len(o) == 1
    print(o[0])
