
from collections import defaultdict, deque
from functools import lru_cache
import heapq
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        cur_line = [char for char in line.strip()]
        res.append(cur_line)
    return res

def solve(pos:tuple[int,int], m:list[list[str]]):
    dirs = {
        '.': [(0,1), (1,0), (0,-1), (-1,0)],
        '>': [(0,1)],
        '<': [(0,-1)],
        '^': [(-1,0)],
        'v': [(1,0)],
        '#': []
    }
    n = len(m)
    # paths = [[-1 for x in range(n)] for y in range(n)]
    # visited = [[-1 for x in range(n)] for y in range(n)]
    ways = deque([(pos,[])])
    res = []
    while len(ways) > 0:
        pos, paths = ways.popleft()
        y,x = pos
        for dir in dirs[m[y][x]]:
            n_y = y + dir[0]
            n_x = x + dir[1]
            if 0 <= n_y < n and 0 <= n_x < n and m[n_y][n_x] != '#':
                if (n_y,n_x) not in paths:
                    new_paths = paths.copy()
                    new_paths.append((n_y,n_x))
                    ways.append(((n_y,n_x), new_paths))
        if (y == n-1 and x == n-2):
            res.append(paths)
    return max(map(len, res))

def main():
    # input = open(r"./2023/23/input_first_test.txt")
    input = open(r"./2023/23/input_first.txt")
    m = parse_input(input.readlines())
    res = solve((0,1), m)
    print(res)

main()