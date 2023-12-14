
from collections import deque
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        res.append([x for x in line.strip()])
        # res.append(line.strip())
    return res

def rotate(input:list[list[str]]):
    n = len(input)
    m = len(input[0])
    res = [['.' for x in range(n)] for y in range(m)]
    for y in range(m):
        for x in range(n):
            res[y][x] = input[n-1-x][y]
    return res

def roll(input:list[list[str]]):
    n = len(input)
    m = len(input[0])
    res = [['.' if input[y][x] in ['.','O'] else '#' for x in range(m)] for y in range(n)]
    for x in range(n):
        r_rocks = 0
        for y in reversed(range(m)):
            if input[y][x] == 'O':
                r_rocks += 1
            elif input[y][x] == '#':
                for i in range(r_rocks):
                    res[y+1+i][x] = 'O'
                r_rocks = 0
        for i in range(r_rocks):
            res[i][x] = 'O'
    return res

def solve(input:list[list[str]]):
    n = len(input)
    m = len(input[0])
    res = 0
    for y in range(n):
        for x in range(m):
            if input[y][x] == 'O':
                res += n-y
    return res

def p_table(t):
    for y in range(len(t)):
        for x in range(len(t[0])):
            print(t[y][x], end="")
        print()


def main():
    mem = {}

    # input = open(r"./2023/14/input_first_test.txt")
    input = open(r"./2023/14/input_first.txt")
    cur = parse_input(input.readlines())
    i = 0
    while i < 10**9:
        i += 1
        for j in range(4):
            cur = roll(cur)
            cur = rotate(cur)
        k = tuple(tuple(r) for r in cur)
        if k in mem:
            repeats = i - mem[k]
            i += ((10**9-i)//repeats) * repeats
        else:
            mem[k] = i
        print(i)
    print(solve(cur))
main()