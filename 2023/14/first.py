
from collections import deque
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        res.append([x for x in line.strip()])
        # res.append(line.strip())
    return res

def solve(input:list[list[str]]):
    res = 0
    res_row = [0] * len(input)
    r_rocks = 0
    r_res = 0
    for x in range(len(input[0])):
        r_rocks = 0
        for y in reversed(range(len(input))):
            if input[y][x] == 'O':
                r_rocks += 1
            # elif input[y][x] == '.':
            #     r_res += r_rocks
            elif input[y][x] == '#':
                for i in range(r_rocks):
                    res += len(input)-y-1-i
                    # res_row[i] += 1
                r_rocks = 0
        for i in range(r_rocks):
            res += (len(input) - i)
        # print(f"{x=}, {res_row=}")
    # res = sum(res_row)
    return res

def main():
    input = open(r"./2023/14/input_first_test.txt")
    # input = open(r"./2023/14/input_first.txt")
    input_lines = parse_input(input.readlines())
    res = solve(input_lines)
    print(res)
main()