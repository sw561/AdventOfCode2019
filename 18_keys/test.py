#!/usr/bin/env python3

from solve import find_path, find_path_part2

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

m = """#########
#b.A.@.a#
#########""".split()

r = find_path(m)
assertEqual(r, 8)

m = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################""".split()

r = find_path(m)
assertEqual(r, 86)

m = """###############
#d.ABC.#.....a#
######@#@######
###############
######@#@######
#b.....#.....c#
###############""".split()

r = find_path_part2(m)
assertEqual(r, 24)

m = """#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba@#@BcIJ#
#############
#nK.L@#@G...#
#M###N#H###.#
#o#m..#i#jk.#
#############""".split()

r = find_path_part2(m)
assertEqual(r, 72)

print("Test passed")
