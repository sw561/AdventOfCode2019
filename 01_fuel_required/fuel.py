#!/usr/bin/env python3

def fuel(mass):
    return mass // 3 - 2

def part1(masses):
    return sum(fuel(m) for m in masses)

def fuel_part2(mass):
    # Calculate addition fuel needed for carrying fuel
    fuel_to_add = fuel(mass)
    total = fuel_to_add
    while fuel_to_add > 0:
        fuel_to_add = max(0, fuel(fuel_to_add))
        total += fuel_to_add

    return total

def part2(masses):
    return sum(fuel_part2(m) for m in masses)

if __name__=="__main__":
    with open("01_fuel_required/input.txt", 'r') as f:
        masses = [int(x) for x in f]

    print(part1(masses))
    print(part2(masses))
