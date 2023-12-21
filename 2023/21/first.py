
from collections import defaultdict, deque
from functools import lru_cache
import heapq
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        res.append([x for x in line.strip()])
    return res

def p_table(t):
    for y in range(len(t)):
        for x in range(len(t[0])):
            print(t[y][x], end="")
        print()

@lru_cache(maxsize=None)
def go(starts:tuple, m:list[list[str]]):
    dirs = [
        (0,1),
        (1,0),
        (0,-1),
        (-1,0)
    ]
    n = len(m)
    new_pos = set()
    for start in starts:
        y,x = start
        for shift_i in dirs:
            n_y = y+shift_i[0]
            n_x = x+shift_i[1]
            if (0 <= n_y < n) and (0 <= n_x < n):
                if m[n_y][n_x] != '#':
                    new_pos.add((n_y, n_x))
    return tuple(new_pos)

def solve(m: list[list[str]], steps):
    n = len(m)
    start = (0,0)
    for y in range(n):
        for x in range(n):
            if m[y][x] == 'S':
                start = (y,x)
    t_m = tuple([tuple(m[y]) for y in range(n)])
    starts = tuple([start])
    for i in range(steps):
        starts = go(starts, t_m)
        print(f"{i+1}: {len(starts)}")
    return len(starts)

def main():
    # input = open(r"./2023/21/input_first_test.txt")
    input = open(r"./2023/21/input_first.txt")
    m = parse_input(input.readlines())
    res = solve(m, 132)
    print(res)

main()