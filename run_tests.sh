#!/usr/bin/env bash
./01_fuel_required/fuel.py | diff 01_fuel_required/output.txt -
./02_program_alarm/prog.py | diff 02_program_alarm/output.txt -
./03_crossed_wires/wires.py | diff 03_crossed_wires/output.txt -
./04_password/password.py | diff 04_password/output.txt -
./05_program_test/prog.py | diff 05_program_test/output.txt -
./06_orbits/orbits.py | diff 06_orbits/output.txt -
./07_amplification/prog.py | diff 07_amplification/output.txt -
./08_space_image/image.py | diff 08_space_image/output.txt -
./09_boost/prog.py | diff 09_boost/output.txt -
