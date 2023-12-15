
from collections import deque
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = lines[0].strip().split(',')
    return res

def solve(input:str):
    res = 0
    for ch in input:
        res += ord(ch)
        res *= 17
        res = res - (res // 256)*256
    return res

def main():
    # input = open(r"./2023/15/input_first_test.txt")
    input = open(r"./2023/15/input_first.txt")
    input_lines = parse_input(input.readlines())
    res = map(solve, input_lines)
    print(sum(res))
main()