
from collections import deque
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        parts = line.strip().split(" ")
        res.append((parts[0], [int(x) for x in parts[1].split(",")]))
    return res

def get_possible_groups(pos:int, cur_group_count:int, collecting_group_ind:int, line:str, remain:list[int]):
    if pos == len(line):
        if (collecting_group_ind == len(remain) and cur_group_count == 0):
            return 1
        elif (collecting_group_ind+1 == len(remain) and cur_group_count == remain[-1]):
            return 1
        else:
            return 0
    if cur_group_count > 0 and (collecting_group_ind >= len(remain) or cur_group_count > remain[collecting_group_ind]):
        return 0
    if line[pos] == ".":
        if cur_group_count == 0:
            return get_possible_groups(pos+1, 0, collecting_group_ind, line, remain)
        elif cur_group_count == remain[collecting_group_ind]:
            return get_possible_groups(pos+1, 0, collecting_group_ind+1, line, remain)
        else:
            return 0
    elif line[pos] == "#":
        return get_possible_groups(pos+1, cur_group_count+1, collecting_group_ind, line, remain)
    elif line[pos] == "?":
        res = 0
        if cur_group_count == 0:
            res += get_possible_groups(pos+1, 0, collecting_group_ind, line, remain)
        elif cur_group_count == remain[collecting_group_ind]:
            res += get_possible_groups(pos+1, 0, collecting_group_ind+1, line, remain)        
        res += get_possible_groups(pos+1, cur_group_count+1, collecting_group_ind, line, remain)
        return res

def solve(input:tuple[str, list[int]]):
    line, groups = input
    res = get_possible_groups(0, 0, 0, line, groups)
    return res

def main():
    # input = open(r"./2023/12/input_first_test.txt")
    input = open(r"./2023/12/input_first.txt")
    input_lines = parse_input(input.readlines())
    res = sum(map(solve, input_lines))
    print(res)

main()