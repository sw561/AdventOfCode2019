#!/usr/bin/env python3

import sys
sys.path.append('.')
from intcode_computer import ProgramInstance
from heapq import heappush, heappop
from collections import deque

def Network(prog, n=50):
    nics = [ProgramInstance(prog) for _ in range(n)]
    queues = [deque([]) for _ in range(n)]
    # Heap used to decide which NIC to run next
    h = []

    for i in range(n):
        out = nics[i].run(inp=i)
        # print(i, out, nics[i].status, nics[i].clock)
        heappush(h, (nics[i].clock, i))

    while h:
        clock, i = heappop(h)

        if queues[i]:
            (x, y) = queues[i].popleft()
            out = nics[i].run(x) + nics[i].run(y)
        else:
            out = nics[i].run(-1)

        # print("Running NIC {}. out = {}".format(i, out))

        assert len(out)%3 == 0
        for j in range(0, len(out), 3):
            index, x, y = out[j:j+3]

            if index==255:
                return y
            else:
                queues[index].append((x, y))

        if nics[i].status == "WAIT":
            heappush(h, (nics[i].clock, i))

def main():
    with open("23_networking/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    part1 = Network(prog)
    print(part1)

if __name__=="__main__":
    main()
