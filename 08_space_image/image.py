#!/usr/bin/env python3

import numpy as np
from collections import Counter
from itertools import dropwhile

def get_layers(width, height, data):
    return np.reshape(data, (-1, height, width))

def part1(layers):
    layer_counts = [Counter(list(np.reshape(layer, -1))) for layer in layers]

    best = min(layer_counts, key=lambda x: x[0])

    return best[1] * best[2]

def part2(layers):
    n, height, width = np.shape(layers)
    for h in range(height):
        for w in range(width):
            x = next(dropwhile(lambda x: x==2, layers[:,h,w])) 
            print('@' if x else ' ', end='')
        print()

if __name__=="__main__":
    
    with open("08_space_image/input.txt", 'r') as f:
        data = np.array([int(x) for x in f.read().strip()])

    layers = get_layers(25, 6, data)

    print(part1(layers))

    part2(layers)
