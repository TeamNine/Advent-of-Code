
from collections import deque
import heapq
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    dirs = {
        "0": "R",
        "1": "D",
        "2": "L",
        "3": "U"
    }
    res = []
    for line in lines:
        parts = line.strip().split(" ")
        instr = parts[2][2:-1]
        dir = dirs[instr[-1]]
        len = int(instr[:-1], 16)
        res.append((dir, len))
    return res
    
def solve(commands:list[tuple[str,int]]):
    dirs = {
        "R" : (0,1),
        "D": (1,0),
        "L": (0,-1),
        "U": (-1,0)
    }
    y = 0
    x = 0
    edges = []
    P = 0
    for command in commands:
        edges.append((y,x))
        P+=command[1]
        y += dirs[command[0]][0]*command[1]
        x += dirs[command[0]][1]*command[1]
    edges.append((y,x))
    print(f"{y=} {x=}")
    
    S = 0
    for i in range(len(edges)-1):
        y1,x1 = edges[i]
        y2,x2 = edges[i+1]
        S += x1*y2-x2*y1
    s_inside = abs(S)//2 - P//2 + 1
    return P+s_inside

def main():
    # input = open(r"./2023/18/input_first_test.txt")
    input = open(r"./2023/18/input_first.txt")
    input_lines = parse_input(input.readlines())
    res = solve(input_lines)
    print(res)

main()