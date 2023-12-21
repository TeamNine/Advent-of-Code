
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
            # if (0 <= n_y < n) and (0 <= n_x < n):
            nn_y = (n_y + n) % n
            nn_x = (n_x + n) % n
            if m[nn_y][nn_x] != '#':
                new_pos.add((n_y, n_x))
    return tuple(new_pos)

def counts_per_grid(starts:tuple, n:int):
    d = defaultdict(int)
    for pos in starts:
        y,x = pos
        n_y, n_x = y//n, x//n
        d[(n_y,n_x)]+=1
    for y in range(5):
        for x in range(5):
            print(f"\t{d.get((y-2,x-2), 0)}", end="")
        print()
    return d

def solve(m: list[list[str]], steps):
    n = len(m)
    start = (0,0)
    for y in range(n):
        for x in range(n):
            if m[y][x] == 'S':
                start = (y,x)
    t_m = tuple([tuple(m[y]) for y in range(n)])
    starts = tuple([start])
    ress = [starts]
    target_s = steps % n + n + n
    for i in range(1,target_s+1):
        ress.append(go(ress[i-1], t_m))
    short_grid = counts_per_grid(ress[target_s], n)
    print(sum(short_grid.values()))
    repeats = (steps // n)-1
    # 1
    #     0       990     5869    978     0
    #     990     6813    7757    6804    978
    #     5846    7757    7748    7757    5846
    #     996     6781    7757    6790    977
    #     0       996     5823    977     0

    # 3
    #     0       0       0       990     5869    978     0       0       0
    #     0       0       990     6813    7757    6804    978     0       0
    #     0       990     6813    7757    7748    7757    6804    978     0
    #     990     6813    7757    7748    7757    7748    7757    6804    978
    #     5846    7757    7748    7757    7748    7757    7748    7757    5846
    #     996     6781    7757    7748    7757    7748    7757    6790    977
    #     0       996     6781    7757    7748    7757    6790    977     0
    #     0       0       996     6781    7757    6790    977     0       0
    #     0       0       0       996     5823    977     0       0       0
    res = (short_grid[(0,0)] * repeats ** 2)+ \
    (short_grid[(0,-1)] * (repeats+1) ** 2)+ \
    ((short_grid[(1,1)] + short_grid[(-1,1)] + short_grid[(-1,-1)] + short_grid[(1,-1)]) * repeats) + \
    ((short_grid[(1,2)] + short_grid[(-1,2)] + short_grid[(-1,-2)] + short_grid[(1,-2)]) * (repeats+1)) + \
    (short_grid[(2,0)] + short_grid[(-2,0)] + short_grid[(0,2)] + short_grid[(0,-2)])
    return res

def main():
    # input = open(r"./2023/21/input_first_test.txt")
    input = open(r"./2023/21/input_first.txt")
    m = parse_input(input.readlines())
    res = solve(m, 26501365)#65 + 131+131+131)#
    print(res)

main()