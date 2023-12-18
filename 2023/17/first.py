
from collections import deque
import heapq
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        res.append([int(x) for x in line.strip()])
    return res

def p_table(t):
    for y in range(len(t)):
        for x in range(len(t[0])):
            print(t[y][x], end="")
        print()

def solve(m:list[list[str]]):
    dirs = [
        (0,1),
        (1,0),
        (0,-1),
        (-1,0)
    ]
    n = len(m)
    seen = set()   
    points = [(0,0,0,-1)]
    costs = {
        (0,0,-1):0
    }
    while points:
        c_cost,y,x,dir = heapq.heappop(points)
        if (y,x,dir) in seen:
            continue
        seen.add((y,x,dir))
        for dir_i in range(len(dirs)):
            if dir_i == dir or (dir_i+2)%4==dir:
                continue
            path_cost = 0 
            for shift_i in range(1,4):
                n_y = y+(dirs[dir_i][0]*shift_i)
                n_x = x+(dirs[dir_i][1]*shift_i)
                if 0<=n_y<n and 0<=n_x<n:
                    path_cost += m[n_y][n_x]
                    if costs.get((n_y,n_x,dir_i), 1e10) <= path_cost+c_cost:
                        continue
                    costs[(n_y,n_x,dir_i)] = path_cost+c_cost
                    heapq.heappush(points, (path_cost+c_cost,n_y,n_x,dir_i))
                else:
                    break
    res = min([costs.get((n-1,n-1,i), 1e10) for i in range(4)])
    return res

def main():
    # input = open(r"./2023/17/input_first_test.txt")
    input = open(r"./2023/17/input_first.txt")
    input_lines = parse_input(input.readlines())
    res = solve(input_lines)
    print(res)

main()