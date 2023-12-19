
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

def mut_rules(start:str, params:tuple, wfs:dict[str, list]):
    if start == "A":
        return [params]
    elif start == "R":
        return []
    param_map = {"x" : 0,"m" : 1,"a" : 2,"s" : 3}
    p_list = list(params)
    results = []
    for rule in wfs[start]:
        if len(rule) == 1:
            if rule[0] == "A":
                results.append(tuple(p_list))
            elif rule[0] != "R":
                results.extend(mut_rules(rule[0], tuple(p_list), wfs))
        else:
            param_ind = param_map[rule[0]]
            cur_p_min, cur_p_max = p_list[param_ind]
            if rule[2] == ">" and cur_p_max > rule[1]:
                go_wf_param = (max(cur_p_min, rule[1]+1), cur_p_max)
                p_list[param_ind] = go_wf_param
                results.extend(mut_rules(rule[3], tuple(p_list), wfs))
                if cur_p_min <= rule[1]:
                    p_list[param_ind] = (cur_p_min, rule[1])
                else:
                    break
            elif rule[2] == "<" and cur_p_min < rule[1]:
                go_wf_param = (cur_p_min, min(cur_p_max, rule[1]-1))
                p_list[param_ind] = go_wf_param
                results.extend(mut_rules(rule[3], tuple(p_list), wfs))
                if cur_p_max >= rule[1]:
                    p_list[param_ind] = (rule[1], cur_p_max)
                else:
                    break
            #go next
    return results

def solve(data: tuple):
    wfs, _= data
    res = 0
    start_p = ((1,4000),(1,4000),(1,4000),(1,4000))
    valid_ranges = mut_rules("in", start_p, wfs)
    for valid_range in valid_ranges:
        range_res = (valid_range[0][1] - valid_range[0][0] + 1)
        for params_range in list(valid_range)[1:]:
            range_res *= (params_range[1] - params_range[0] + 1)
        res += range_res
    return res

def main():
    # input = open(r"./2023/19/input_first_test.txt")
    input = open(r"./2023/19/input_first.txt")
    input_data = parse_input(input.readlines())
    res = solve(input_data)
    print(res)

main()