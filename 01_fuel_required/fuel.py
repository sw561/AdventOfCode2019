#!/usr/bin/env python3

def fuel(mass):
    return max(0, mass // 3 - 2)

def fuel_part2(mass):
    # Calculate additional fuel needed for carrying fuel
    total = 0
    while mass > 0:
        mass = fuel(mass)
        total += mass
    return total

if __name__=="__main__":
    with open("01_fuel_required/input.txt", 'r') as f:
        masses = [int(x.strip()) for x in f]

    print(sum(fuel(m) for m in masses))
    print(sum(fuel_part2(m) for m in masses))
