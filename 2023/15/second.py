
from collections import deque
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = lines[0].strip().split(',')
    return res

def HASH(input:str):
    res = 0
    for ch in input:
        res += ord(ch)
        res *= 17
        res = res - (res // 256)*256
    return res

def solve(input:list[str]):
    res = [[] for i in range(256)]
    for label in input:
        if label[-1] == '-':
            l = label[:-1]
            h = HASH(l)
            found = -1
            for i in range(len(res[h])):
                if res[h][i][0] == l:
                    found = i
            if found != -1:
                del res[h][found]
        else:
            f = int(label[-1])
            l = label[:-2]
            h = HASH(l)
            found = -1
            for i in range(len(res[h])):
                if res[h][i][0] == l:
                    found = i
            if found != -1:
                res[h][found] = (l, f)
            else:
                res[h].append((l, f))

    for i, x in enumerate(res):
        if x:
            print(f"{i=}, {x=}")                
    p = 0
    for i, x in enumerate(res):
        for j, xx in enumerate(x):
            p += (i+1) * (j+1) * xx[1]
    return p

def main():
    # input = open(r"./2023/15/input_first_test.txt")
    input = open(r"./2023/15/input_first.txt")
    input_lines = parse_input(input.readlines())
    res = solve(input_lines)
    print(res)
main()