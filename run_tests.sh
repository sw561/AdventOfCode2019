#!/usr/bin/env bash
./01_fuel_required/fuel.py | diff 01_fuel_required/output.txt -
./01_fuel_required/test.py
./02_program_alarm/prog.py | diff 02_program_alarm/output.txt -
./02_program_alarm/test.py
./03_crossed_wires/wires.py | diff 03_crossed_wires/output.txt -
./03_crossed_wires/test.py
./04_password/password.py | diff 04_password/output.txt -
./05_program_test/prog.py | diff 05_program_test/output.txt -
./05_program_test/test.py
./06_orbits/orbits.py | diff 06_orbits/output.txt -
./06_orbits/test.py
./07_amplification/prog.py | diff 07_amplification/output.txt -
./07_amplification/test.py
./08_space_image/image.py | diff 08_space_image/output.txt -
./08_space_image/test.py
./09_boost/prog.py | diff 09_boost/output.txt -
./09_boost/test.py
./10_asteroids/solve.py | diff 10_asteroids/output.txt -
./10_asteroids/test.py
./11_robot/solve.py | diff 11_robot/output.txt -
./12_three_body/solve.py | diff 12_three_body/output.txt -
./12_three_body/test.py
./13_arcade/solve.py | diff 13_arcade/output.txt -
./14_chemicals/solve.py | diff 14_chemicals/output.txt -
./14_chemicals/test.py
./15_exploration/solve.py | diff 15_exploration/output.txt -
./16_fft/solve.py | diff 16_fft/output.txt -
./16_fft/test.py
