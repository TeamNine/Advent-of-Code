
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

def dfs(pos, d, sh, seen, last):
    if pos == last:
        print(f"New path: {d}, S: {len(seen)}")
        return d
    seen.add(pos)
    res = -1
    for next_pos, next_path in sh[pos].items():
        if next_pos not in seen:
            new_d = dfs(next_pos, d + len(next_path) - 1, sh, seen, last)
            res = max(new_d, res)
    seen.remove(pos)
    return res

def solve(m:list[list[str]]):
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    n = len(m)
    start = (0,1)
    end = (n-1, n-2)    
    gates = [start, end]
    for y in range(n):
        for x in range(n):
            if m[y][x] == '#':
                continue
            near = 0
            for dir in dirs:
                n_y = y + dir[0]
                n_x = x + dir[1]
                if 0 <= n_y < n and 0 <= n_x < n and m[n_y][n_x] != '#':
                    near += 1
            if near > 2:
                gates.append((y,x))

    sh = defaultdict(dict)
    for gate in gates:
        ways = deque([(gate, [])]) 
        seen = set()
        while ways:
            pos, path = ways.popleft()
            if pos in seen:
                continue
            seen.add(pos)
            path.append(pos)
            if pos in gates and pos != gate:
                sh[path[0]][pos] = path.copy()
                sh[pos][path[0]] = list(reversed(path))
                continue
            y,x = pos      
            for dir in dirs:
                n_y = y + dir[0]
                n_x = x + dir[1]
                if 0 <= n_y < n and 0 <= n_x < n and m[n_y][n_x] != '#':
                    if (n_y,n_x) not in path:
                        ways.append(((n_y,n_x), path.copy()))
    for k,v in sh.items():
        print(f"{k=}")
        for vv, pp in v.items():
            print(f"\t{vv=}, {pp=}")
    res = dfs(start, 0, sh, set(), end)
    return res

def main():
    # input = open(r"./2023/23/input_first_test.txt")
    input = open(r"./2023/23/input_first.txt")
    m = parse_input(input.readlines())
    res = solve(m)
    print(res)

main()