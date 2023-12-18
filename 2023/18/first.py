
from collections import deque
import heapq
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        parts = line.strip().split(" ")
        res.append((parts[0], int(parts[1]), parts[2][2:-1]))
    return res

def p_table(t):
    for y in range(len(t)):
        for x in range(len(t[0])):
            print(t[y][x], end="")
        print()

def get_size(commands:list[tuple[str,int,str]]):
    dirs = {
        "R" : (0,1),
        "D": (1,0),
        "L": (0,-1),
        "U": (-1,0)
    }
    pos_x = 0
    pos_y = 0
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for command in commands:
        dir, len, color = command
        pos_y += dirs[dir][0]*len
        pos_x += dirs[dir][1]*len
        min_y = min(pos_y, min_y)
        max_y = max(pos_y, max_y)
        min_x = min(pos_x, min_x)
        max_x = max(pos_x, max_x)
    return (max_y-min_y)+1, (max_x-min_x)+1, 0-min_y, 0-min_x

def fill_map(m:list[list[int]], start):
    dirs = [
        (0,1),
        (1,0),
        (0,-1),
        (-1,0)
    ]
    points = deque([start])
    while points:
        y,x = points.popleft()
        if m[y][x] == 1:
            continue
        for dir in dirs:
            if m[y+dir[0]][x+dir[1]] == 0:
                m[y+dir[0]][x+dir[1]] = 2
                points.append((y+dir[0], x+dir[1]))
    # for y in range(len(m)):
    #     if y>0 and m[y-1][0] != 0:
    #         in_loop = True
    #     else:
    #         in_loop = False
    #     last_border = False
    #     for x in range(len(m[0])):
    #         if (m[y][x] == 1):
    #             if last_border:
    #                 # border case
    #                 in_loop = False
    #                 continue
    #             else:
    #                 last_border = True
    #                 in_loop = not in_loop
    #         else:
    #             if in_loop:
    #                 m[y][x] = 2
    #             last_border = False
    return m

def create_map(commands:list[tuple[str,int,str]]):
    dirs = {
        "R" : (0,1),
        "D": (1,0),
        "L": (0,-1),
        "U": (-1,0)
    }
    n,m,start_y,start_x = get_size(commands)
    m = [[0 for x in range(m)]for y in range(n)]
    pos_y = start_y
    pos_x = start_x
    m[pos_y][pos_x] = 1
    for command in commands:
        dir, len, color = command
        for i in range(1,len+1):
            pos_y += dirs[dir][0]
            pos_x += dirs[dir][1]
            m[pos_y][pos_x] = 1
    return m, (start_y, start_x)
    
def solve(commands:list[tuple[str,int,str]]):
    res = 0
    m, start  = create_map(commands)
    # p_table(m)
    fill_map(m, (start[0]-1, start[1]))
    # print()
    # p_table(m)
    for y in range(len(m)):
        for x in range(len(m[0])):
            res += 1 if m[y][x] != 0 else 0
    return res

def main():
    # input = open(r"./2023/18/input_first_test.txt")
    input = open(r"./2023/18/input_first.txt")
    input_lines = parse_input(input.readlines())
    res = solve(input_lines)
    print(res)

main()