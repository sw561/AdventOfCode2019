#!/usr/bin/env python3

from solve import process_input, reduce, mul # , get_position, get_card

def compare_deck(d1, d2):
    for c1, c2 in zip(d1, d2):
        try:
            assert c1 == c2
        except AssertionError:
            print(d1)
            print(d2)
            raise

def construct_deck(fs, nshuffle=1):
    n = fs[0].n
    deck = [None]*n
    composed_f = reduce(mul, reversed(fs))
    temp = composed_f
    for i in range(nshuffle-1):
        temp *= composed_f
    composed_f = temp

    # print("c", composed_f)
    for i in range(n):
        p = composed_f(i)
        if deck[p] is not None:
            raise
        deck[p] = i
    return deck

def test(f, expected_out):
    f = f.split('\n')

    # Compare with given output
    fs, inv_fs = process_input(f, 10)

    deck = construct_deck(fs)
    compare_deck(deck, [int(x) for x in expected_out.split()])

    # Compare fowards with backwards calculation
    fs, inv_fs = process_input(f, 11)
    composed_inv = reduce(mul, inv_fs)

    deck1 = construct_deck(fs)
    deck2 = map(composed_inv, range(11))

    compare_deck(deck1, deck2)

    # Compare clever pow with explicit mul
    deck1 = construct_deck(fs, 21)
    composed_inv = composed_inv**21
    deck2 = map(composed_inv, range(11))

    compare_deck(deck1, deck2)

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
