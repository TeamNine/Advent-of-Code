
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
    expanded_columns = [i for i,x in enumerate(columns) if x == 0]
    expanded_rows = [i for i,y in enumerate(rows) if y == 0]
    return expanded_columns, expanded_rows

def solve(space:list[list[str]]):
    res = 0
    starts = []
    for y in range(len(space)):
        for x in range(len(space[y])):
            if space[y][x] == '#':
                starts.append((y,x))
    expanded_columns, expanded_rows = expand(space)
    for i, start in enumerate(starts):
        for ii in range(i+1, len(starts)):
            distance = 0
            min_y = min(start[0], starts[ii][0])
            max_y = max(start[0], starts[ii][0])
            for d_y in range(min_y, max_y):
                distance += 1 if (d_y+1) not in expanded_rows else 1000000
            min_x = min(start[1], starts[ii][1])
            max_x = max(start[1], starts[ii][1])                
            for d_x in range(min_x, max_x):
                distance += 1 if (d_x+1) not in expanded_columns else 1000000
            res += distance
    return res

def main():
    # input = open(r"./2023/11/input_first_test.txt")
    input = open(r"./2023/11/input_first.txt")
    input_lines = parse_input(input.readlines())
    # space = expand(input_lines)
    res = solve(input_lines)
    print(res)

main()