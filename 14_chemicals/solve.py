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

    return reactants, products, reactions

def calculate_priorities(reactants, products):
    priorities = []

    q = deque(['ORE'])

    while q:
        done = q.popleft()

        for p in products[done]:
            reactants[p].remove(done)

            if not reactants[p]:
                # We now have all the ingredients to produce p
                q.append(p)
                priorities.append(p)

    return priorities

def solve(priorities, reactions, n_fuel=1, part2=False):
    # We want to start with n ore and end with 1 fuel and some left over
    # materials.
    #
    # We will work it out backwards, which means we start with 1 fuel and will
    # end up with negative or zero amounts of everything except ORE.

    amounts = defaultdict(int)
    amounts['FUEL'] = n_fuel

    for chemical in reversed(priorities):
        # we have amounts[chemical]
        # we need to do reactions backwards until amount[chemical] <= 0

        # Use the unique reaction which produces chemical
        n, reactants = reactions[chemical]

        # Number of times we will need to run reaction
        if not part2:
            k = ceil(amounts[chemical] / n)
        else:
            k = amounts[chemical] / n

        amounts[chemical] -= n * k
        for r, rn in reactants.items():
            amounts[r] += rn * k

        # print("{} {} {} carried out {} times".format(n, chemical, reactants, k))

    if not part2:
        return amounts['ORE']

    return int(1e12 / amounts['ORE'])

if __name__=="__main__":
    with open("14_chemicals/input.txt", 'r') as f:
        reactants, products, reactions = process_input(f)

    p = calculate_priorities(reactants, products)

    print(solve(p, reactions))

    nf = solve(p, reactions, part2=True)
    nfo = solve(p, reactions, n_fuel=nf)
    if nfo > 1e12:
        while nfo > 1e12:
            nf -= 1
            nfo = solve(p, reactions, n_fuel=nf)
    else:
        while solve(p, reactions, n_fuel=nf+1) <= 1e12:
            nf += 1

    print(nf)
