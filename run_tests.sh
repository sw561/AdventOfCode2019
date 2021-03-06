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
./17_ascii/solve.py | diff 17_ascii/output.txt -
./17_ascii/test.py
./18_keys/solve.py | diff 18_keys/output.txt -
./18_keys/test.py
./19_tractor_beam/solve.py | diff 19_tractor_beam/output.txt -
./20_donut/solve.py | diff 20_donut/output.txt -
./20_donut/test.py
./21_springdroid/solve.py | diff 21_springdroid/output.txt -
./22_shuffling/solve.py | diff 22_shuffling/output.txt -
./22_shuffling/test.py
./23_networking/solve.py | diff 23_networking/output.txt -
./24_bugs/solve.py | diff 24_bugs/output.txt -
./24_bugs/test.py
./25_game/solve.py 25_game/attempt | grep keypad | grep -Eo "[0-9]+" | diff 25_game/output.txt -
