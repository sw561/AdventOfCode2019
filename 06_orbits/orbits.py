#!/usr/bin/env python3

from collections import defaultdict

def part1(children):
    # do a breadth first search to get generation of each node

    nodes = ['COM']
    orbits = 0
    g = 0

    while nodes:
        g += 1
        new_nodes = []
        for node in nodes:
            new_nodes += children[node]
            orbits += g * len(children[node])

        nodes = new_nodes

    return orbits

def parent_list(parents, node):
    p = [node]
    while node != 'COM':
        node = parents[node]
        p.append(node)
    return p

def route(parents, start, end):

    # Construct a list of parents for each of start and end
    ps = parent_list(parents, start)
    pe = parent_list(parents, end)

    # Now remove any matching parents
    while ps and pe and ps[-1] == pe[-1]:
        ps.pop()
        pe.pop()

    return len(ps) + len(pe)

def processInput(fname):
    # Dict containing children of each item
    children = defaultdict(list)
    parents = dict()
    with open(fname, 'r') as f:
        for line in f:
            parent, child = (x for x in line.strip().split(')'))
            children[parent].append(child)
            parents[child] = parent

    return children, parents

if __name__=="__main__":

    children, parents = processInput("06_orbits/input.txt")
    print(part1(children))

    print(route(parents, parents['YOU'], parents['SAN']))
