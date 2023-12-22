
from collections import deque
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        cur_line = [char for char in line.strip()]
        res.append(cur_line)
    return res

def add_borders(field:list[list[str]]) -> list[list[str]]:
    n = len(field)
    m = len(field[0])
    res = []
    for y in range(n+2):
        if y in [0, n+1]:
            res.append(["#" for i in range(m+2)])
            continue
        res.append(["#", *field[y-1], "#"])
    return res        

def get_start_point(b_map:list[list[str]]):
    for y in range(len(b_map)):
        for x in range(len(b_map[y])):
            if b_map[y][x] == "S":
                return y,x

def distance_map(b_map:list[list[str]], y:int, x:int):
    pipe_map = {
        ".": [],
        "#": [],
        "F": [(0,1),(+1,0)],
        "7": [(0,-1),(+1,0)],
        "-": [(0,-1),(0,+1)],
        "|": [(-1,0),(+1,0)],
        "J": [(-1,0),(0,-1)],
        "L": [(-1,0),(0,+1)],
        "S": [(-1,0), (1,0), (0,-1), (0,1)]
    }
    distance_map = []
    for yy in range(len(b_map)):
        line = []
        for xx in range(len(b_map[yy])):
            line.append(-1)
        distance_map.append(line)
    queue = deque([(y,x,y,x)])
    distance_map[y][x] = 0
    while len(queue)>0:
        y,x, y1, x1 = queue.popleft()
        char = b_map[y][x]
        for poss in pipe_map[char]:
            cur_distance = distance_map[y+poss[0]][x+poss[1]]
            if b_map[y+poss[0]][x+poss[1]] in [".", "#", "S"]:
                continue
            if (y+poss[0],x+poss[1]) == (y1,x1):
                continue
            if cur_distance==-1 or cur_distance>=distance_map[y][x]+1:
                distance_map[y+poss[0]][x+poss[1]] = distance_map[y][x]+1
                queue.append((y+poss[0],x+poss[1], y,x))
    return distance_map

def solve(b_map:list[list[str]]):
    res = 0
    start_y, start_x = get_start_point(b_map)
    b_map[start_y][start_x] = "#"
    for shift in [(1,0), (-1,0), (0,1), (0,-1)]:
        d_map = distance_map(b_map, start_y+shift[0], start_x+shift[1])
        res = max(res, (max(map(max, d_map))+2)//2)
    return res
        
def main():
    # input = open(r"./2023/10/input_first_test.txt")
    input = open(r"./2023/10/input_first.txt")
    input_lines = parse_input(input.readlines())
    b_map = add_borders(input_lines)
    # print(b_map)
    res = solve(b_map)
    print(res)

main()