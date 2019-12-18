#!/usr/bin/env python3

from solve import solve

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

m = """#########
#b.A.@.a#
#########""".split()

r = solve(m, '@')
assertEqual(r, 8)

m = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################""".split()

r = solve(m, '@')
assertEqual(r, 86)

m = """###############
#d.ABC.#.....a#
######1#2######
###############
######3#4######
#b.....#.....c#
###############""".split()

r = solve(m, '1234')
assertEqual(r, 24)

m = """#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba1#2BcIJ#
#############
#nK.L3#4G...#
#M###N#H###.#
#o#m..#i#jk.#
#############""".split()

r = solve(m, '1234')
assertEqual(r, 72)

print("Test passed")
