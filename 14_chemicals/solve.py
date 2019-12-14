#!/usr/bin/env python3

from collections import defaultdict, deque
from math import ceil

def process_input(f):
    # reactants[x] is set of ingredients needed to make x
    reactants = defaultdict(set)
    # products[r] is a list of things which we can build using r
    products = defaultdict(list)

    # reactions[c] = [x, {a: p, b: q}] means we have a reaction
    # p a, q b => x c
    # for chemicals a, b, c and numbers p, q, x
    reactions = defaultdict(lambda: [0, dict()])

    for line in f:
        reac, prod = line.replace('>', '').split('=')

        prod = prod.split(',')
        n, p = prod[0].split()
        reactions[p][0] = int(n)

        reac = reac.split(',')
        for r in reac:
            n, x = r.split()
            reactants[p].add(x)
            products[x].append(p)
            reactions[p][1][x] = int(n)

        # print(reac, prod)

    return reactants, products, reactions

def calculate_priorities(reactants, products):
    priorities = []

    q = deque(['ORE'])

    while q:
        done = q.popleft()

        for p in products[done]:
            reactants[p].remove(done)

            if not reactants[p]:
                q.append(p)
                priorities.append(p)

    return priorities

def solve(priorities, reactions):
    # We want to start with n ore and end with 1 fuel and some left over
    # materials.
    #
    # We will work it out backwards, which means we start with 1 fuel and will
    # end up with negative or zero amounts of everything except ORE.

    amounts = defaultdict(int)
    amounts['FUEL'] = 1
    # print(amounts)

    for chemical in reversed(priorities):
        # we have amounts[chemical]
        # we need to do reactions backwards until amount[chemical] <= 0

        # Use the unique reaction which produces chemical
        n, reactants = reactions[chemical]

        # Number of times we will need to run reaction
        k = ceil(amounts[chemical] / n)

        amounts[chemical] -= n * k
        for r, rn in reactants.items():
            amounts[r] += rn * k

        print("{} {} {} carried out {} times".format(n, chemical, reactants, k))
        # print(amounts)

    return amounts['ORE']

if __name__=="__main__":
    with open("14_chemicals/input.txt", 'r') as f:
        reactants, products, reactions = process_input(f)

    p = calculate_priorities(reactants, products)
    print(solve(p, reactions))
