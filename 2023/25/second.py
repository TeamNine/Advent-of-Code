
from collections import defaultdict, deque
from functools import lru_cache
import heapq
import math
import re
import z3

def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        parts = line.strip().split('@')
        pos = tuple(map(int, parts[0].split(', ', 2)))
        v = tuple(map(int, parts[1].split(', ', 2)))
        res.append((pos, v))
    return res

def solve(a:list[tuple[tuple[int,int,int], tuple[int,int,int]]]):
    s = z3.Solver()
    r_x, r_y, r_z = z3.Ints('rx ry rz')
    r_vx, r_vy, r_vz = z3.Ints('rvx rvy rvz')
    for i,line in enumerate(a[:3]):
        pos, v = line
        x, y, z = pos
        vx, vy, vz = v
        t = z3.Int(f"t{i}")
        s.add(x + t * vx == r_x + t * r_vx, t >= 0)
        s.add(y + t * vy == r_y + t * r_vy, t >= 0)
        s.add(z + t * vz == r_z + t * r_vz, t >= 0)
    if str(s.check()) != 'sat':
        print("Can not calculate")
    else:
        print(s.model())
        return s.model().evaluate(r_x+r_y+r_z)
    return 0

def main():
    # input = open(r"./2023/24/input_first_test.txt")
    input = open(r"./2023/24/input_first.txt")
    m = parse_input(input.readlines())
    res = solve(m)
    print(res)

main()