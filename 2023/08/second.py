
import itertools
import math
import re


def parse_input(lines: list[str]) -> list[tuple[str,int]]:
    navigation = lines[0].strip()
    navigation_map = {}
    for line in lines[2:]:
        if found:=re.match(r"^(?P<from>.*?) = \((?P<L>.*?), (?P<R>.*?)\)$", line.strip()):
            navigation_map[found.group("from")] =  (found.group("L"), found.group("R"))
    return navigation, navigation_map

def get_z_pos(pos, dirs, n_map):
    step = 0
    while pos[2]!="Z":
        pos = n_map[pos][next(dirs)]
        step += 1
    return step

def solve(instruction, navigation_map):
    dirs = [0 if x == "L" else 1 for x in instruction]
    res = -1
    z = [[get_z_pos(pos, itertools.cycle(dirs), navigation_map)] for pos in navigation_map.keys() if pos.endswith("A")]
    for cmb in itertools.product(*z):
        lcm = math.lcm(*cmb)
        res = lcm if res == -1 else min(res, lcm)
    return res
        
def main():
    # input = open(r"./2023/08/input_second_test.txt")
    input = open(r"./input_first.txt")
    instruction, naviagation_map = parse_input(input.readlines())
    res = solve(instruction, naviagation_map)
    print(res)

main()