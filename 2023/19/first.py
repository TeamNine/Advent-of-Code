
from collections import deque
import heapq
import re

def pars_command(cmd):
    if "<" in cmd or ">" in cmd:
        label = cmd.find(":")
        prop = cmd[0]
        param = int(cmd[2:label])
        next_wf = cmd[label+1:]
        operation = cmd[1]
        return (prop, param, operation, next_wf)
    return (cmd,)

def parse_input(lines: list[str]) -> list[list[str]]:
    wfs = {}
    parts = []
    start = ""
    isParts = False
    for line in lines:
        line = line.strip()
        if line == '':
            isParts = True
            continue
        if not isParts:
            bracket_ind = line.find("{")
            rules = [pars_command(c) for c in line[bracket_ind+1:-1].split(",")]
            wfs[line[:bracket_ind]] = rules
            if not start:
                start = line[:bracket_ind]
        else:
            params = {l[0]:int(l[2:]) for l in line[1:-1].split(",")}
            parts.append(params)
    return (wfs, parts)

def emulate(part:dict[str, int], wfs:dict[str, list], start:str = "in"):
    cur_cmd = start
    while cur_cmd not in ["A","R"]:
        print(f" -> {cur_cmd}", end="")
        rules = wfs[cur_cmd]
        for rule in rules:
            if len(rule) == 1:
                cur_cmd = rule[0]
                break
            else:
                diff = part[rule[0]] - rule[1]
                if (rule[2] == ">" and diff > 0) or (rule[2] == "<" and diff < 0):
                    cur_cmd = rule[3]
                    break
    print(f" --> {cur_cmd}")
    return cur_cmd

def solve(data: tuple):
    wfs, parts= data
    res = 0
    for part in parts:
        e_res = emulate(part, wfs)
        if e_res == "A":
            res += part["x"]+part["m"]+part["a"]+part["s"]
    return res

def main():
    # input = open(r"./2023/19/input_first_test.txt")
    input = open(r"./2023/19/input_first.txt")
    input_data = parse_input(input.readlines())
    res = solve(input_data)
    print(res)

main()