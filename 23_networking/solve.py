#!/usr/bin/env python3

import sys
sys.path.append('.')
from intcode_computer import ProgramInstance
from heapq import heappush, heappop
from collections import deque

def network(prog, n=50):
    part1 = None

    nics = [ProgramInstance(prog) for _ in range(n)]
    queues = [deque([]) for _ in range(n)]
    # Heap used to decide which NIC to run next
    h = []

    NAT_memory = (None, None)
    part2_seen = set()

    idle = [False]*n

    for i in range(n):
        out = nics[i].run(inp=i)
        # assert len(out) == 0
        heappush(h, (nics[i].clock, i))

    while h:
        clock, i = heappop(h)

        if queues[i]:
            (x, y) = queues[i].popleft()
            out = nics[i].run(x) + nics[i].run(y)
        else:
            out = nics[i].run(-1)

        # print("Running NIC {}. out = {}".format(i, out))

        # assert len(out)%3 == 0
        if len(out) == 0:
            idle[i] = True
            if all(idle) and not any(queues):
                # print("Sending NAT message", NAT_memory)
                if NAT_memory[1] in part2_seen:
                    print(NAT_memory[1])
                    return
                else:
                    part2_seen.add(NAT_memory[1])
                queues[0].append(NAT_memory)
        else:
            idle[i] = False

        for j in range(0, len(out), 3):
            index, x, y = out[j:j+3]

            if index==255:
                if part1 is None:
                    part1 = y
                    print(part1)
                NAT_memory = (x, y)
            else:
                queues[index].append((x, y))

        heappush(h, (nics[i].clock, i))

if __name__=="__main__":
    with open("23_networking/input.txt", 'r') as f:
        prog = [int(x) for x in f.read().split(',')]

    network(prog)
