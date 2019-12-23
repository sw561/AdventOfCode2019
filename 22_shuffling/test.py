#!/usr/bin/env python3

from solve import process_input, get_position

def compare_deck(d1, d2):
    for c1, c2 in zip(d1, d2):
        try:
            assert c1 == c2
        except AssertionError:
            print(d1)
            print(d2)
            raise

def construct_deck(fs, n):
    deck = [None]*n
    for i in range(n):
        p = get_position(fs, i, n)
        if not deck[p] is None:
            raise
        deck[p] = i
    return deck

def test(f, expected_out):
    f = f.split('\n')

    fs = process_input(f)
    # for f in fs:
    #     print(f, f.__name__)

    deck = construct_deck(fs, 10)
    compare_deck(deck, [int(x) for x in expected_out.split()])

f = """
deal with increment 7
deal into new stack
deal into new stack"""
test(f, "0 3 6 9 2 5 8 1 4 7")

f = """
cut 3"""
test(f, "3 4 5 6 7 8 9 0 1 2")

f = """
cut 6
deal with increment 7
deal into new stack"""

test(f, "3 0 7 4 1 8 5 2 9 6")

f = """
deal with increment 7
deal with increment 9
cut -2"""

test(f, "6 3 0 7 4 1 8 5 2 9")

f = """
deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1"""

test(f, "9 2 5 8 1 4 7 0 3 6")

print("Test passed")
