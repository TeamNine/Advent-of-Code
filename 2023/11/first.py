
from collections import deque
import re


def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        res.append([x for x in line.strip()])
    return res

def expand(space:list[list[str]]) -> list[list[str]] :
    columns = [sum(1 if space[y][x] == '#' else 0 for y in range(len(space))) for x in range(len(space[0])) ]
    rows = [sum(1 if space[y][x] == '#' else 0 for x in range(len(space[y]))) for y in range(len(space))]

    for x, val in reversed(list(enumerate(columns))):
        if val == 0:
            for y in range(len(space)):
                space[y].insert(x, '.')
    for y, val in reversed(list(enumerate(rows))):
        if val == 0:
            space.insert(y, ['.' for x in range(len(space[0]))])
    # for y in range(len(space)):
    #     for x in range(len(space[y])):
    #         print(space[y][x], end="")
    #     print()
    return space

def distance_map(start, space:list[list[str]]):
    d_map = []
    for y in range(len(space)):
        d_map.append([-1 for x in range(len(space[y]))])
    d_map[start[0]][start[1]] = 0
    queue = deque([start])
    while queue:
        y, x = queue.popleft()
        for shift in [(1,0), (-1,0), (0,1), (0,-1)]:
            if not ((y + shift[0]) in range(len(space)) and (x + shift[1]) in range(len(space[0]))):
                continue
            if d_map[y + shift[0]][x + shift[1]] == -1 or d_map[y + shift[0]][x + shift[1]] > d_map[y][x]+1:
                d_map[y + shift[0]][x + shift[1]] = d_map[y][x]+1
                queue.append((y + shift[0],x + shift[1]))
    return d_map

def solve(space:list[list[str]]):
    res = 0
    starts = []
    for y in range(len(space)):
        for x in range(len(space[y])):
            if space[y][x] == '#':
                starts.append((y,x))
    for i, start in enumerate(starts):
        d_map = distance_map(start, space)
        for ii in range(i, len(starts)):
            res += d_map[starts[ii][0]][starts[ii][1]]
    return res

def main():
    # input = open(r"./2023/11/input_first_test.txt")
    input = open(r"./2023/11/input_first.txt")
    input_lines = parse_input(input.readlines())
    space = expand(input_lines)
    res = solve(space)
    print(res)

main()