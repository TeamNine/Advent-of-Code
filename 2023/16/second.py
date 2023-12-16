
from collections import deque
import itertools
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

def go(pos:tuple[int,int], m:list[list[str]], dir:int):
    dirs = [
        (0,1),
        (1,0),
        (0,-1),
        (-1,0)
    ]
    n = len(m)
    paths = [[[] for x in range(n)] for y in range(n)]
    ways = deque([(pos,dir)])
    while len(ways) > 0:
        pos,dir = ways.popleft()
        while (0 <= pos[0] < n) and (0 <= pos[1] < n):
            y,x = pos
            if (dir in paths[y][x]):
                break
            paths[y][x].append(dir)
            if m[y][x] == '.':
                pos = (y+dirs[dir][0], x+dirs[dir][1])
            if dir in [1,3]:
                if m[y][x] == '-':
                    ways.append(((y+dirs[0][0], x+dirs[0][1]), 0))
                    ways.append(((y+dirs[2][0], x+dirs[2][1]), 2))
                    break
                if m[y][x] == '|':
                    pos = (y+dirs[dir][0], x+dirs[dir][1])
                if m[y][x] == '/':
                    dir = (dir + 1)%4
                    pos = (y+dirs[dir][0], x+dirs[dir][1])
                if m[y][x] == '\\':
                    dir = (dir + 3)%4
                    pos = (y+dirs[dir][0], x+dirs[dir][1])
            elif dir in [0,2]:
                if m[y][x] == '-':
                    pos = (y+dirs[dir][0], x+dirs[dir][1])
                if m[y][x] == '|':
                    ways.append(((y+dirs[1][0], x+dirs[1][1]), 1))
                    ways.append(((y+dirs[3][0], x+dirs[3][1]), 3))
                    break
                if m[y][x] == '/':
                    dir = (dir + 3)%4
                    pos = (y+dirs[dir][0], x+dirs[dir][1])
                if m[y][x] == '\\':
                    dir = (dir + 1)%4
                    pos = (y+dirs[dir][0], x+dirs[dir][1])
    return paths

def solve(input:list[list[str]]):
    n = len(input)
    best_res = 0

    possible_starts = [
        *itertools.product([0], range(n), [1]),
        *itertools.product(range(n), [n-1], [2]),
        *itertools.product([n-1], range(n), [3]),
        *itertools.product(range(n), [0], [0])
    ]
    for start in possible_starts:
        paths = go((start[0], start[1]), input, start[2])
        res = [[0 for x in range(len(input))] for y in range(len(input))]
        for y in range(len(paths)):
            for x in range(len(paths[0])):
                res[y][x] += len(paths[y][x])
        # p_table(res)
        res_c = 0
        for y in range(len(res)):
            for x in range(len(res[0])):
                if res[y][x] != 0:
                    res_c+=1
        print(res_c)
        best_res = max(best_res,res_c)
    return best_res

def main():
    # input = open(r"./2023/16/input_first_test.txt")
    input = open(r"./2023/16/input_first.txt")
    input_lines = parse_input(input.readlines())
    res = solve(input_lines)
    print(res)

main()