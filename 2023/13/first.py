
from collections import deque
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    tmp = []
    for line in lines:
        if line.strip() == '':
            res.append(tmp)
            tmp = []
            continue
        #tmp.append([x for x in line.strip()])
        tmp.append(line.strip())
    res.append(tmp)
    return res

def turn(input:list[list[str]]):
    res = [""] * len(input[0])
    for y in range(len(input)):
        for x in range(len(input[y])):
            res[x] += input[y][x]
    return res

def check(input:list[list[str]], pos):
    mir_pos = pos+1
    bad = 0 
    while 0<=pos and mir_pos<len(input):
        if input[pos] != input[mir_pos]:
            for x in range(len(input[pos])):
                if input[pos][x] != input[mir_pos][x]:
                    bad += 1
        pos -= 1
        mir_pos +=1        
    return bad

def solve(input:list[list[str]]):
    t_input = turn(input)
    v_res = -1
    h_res = -1
    res = 0
    for i in range(len(t_input)-1):
        if t_input[i] == t_input[i+1]:
            if check(t_input, i) == 0:
                # print(f"{i=}")
                v_res = i+1
                res += v_res
            
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            if check(input, i) == 0:
                # print(f"{i=} 100")
                h_res = i+1
                res += (h_res*100)
    # res = max(h_res, v_res)
    # return res if res == v_res else h_res*100
    return res

def main():
    # input = open(r"./2023/13/input_first_test.txt")
    input = open(r"./2023/13/input_first.txt")
    input_lines = parse_input(input.readlines())
    res = sum(map(solve, input_lines))
    print(res)

main()