
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
            line.append(-2)
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
            if cur_distance==-2 or cur_distance>=distance_map[y][x]+1:
                distance_map[y+poss[0]][x+poss[1]] = distance_map[y][x]+1
                queue.append((y+poss[0],x+poss[1], y,x))
    return distance_map

def restore_path(end, d_map:list[list[str]], b_map:list[list[str]]):
    pipe = [[0 for x in range(len(d_map[0]))] for y in range(len(d_map))] 
    y,x = end
    while d_map[y][x] != 0:
        # pipe[y+shift[0]][x+shift[1]] = 1
        pipe[y][x] = 1
        for shift in [(1,0), (-1,0), (0,1), (0,-1)]:
            if d_map[y+shift[0]][x+shift[1]] + 1 == d_map[y][x]:
                y,x = (y+shift[0], x+shift[1])
                break
    pipe[y][x] = 1

    for y in range(len(pipe)):
        for x in range(len(pipe[y])):
            print(pipe[y][x], end="")
        print()
    return pipe

def count_inner(pipe_map:list[list[str]], b_map:list[list[str]]):
    count = 0
    for y in range(len(pipe_map)):
        inner = False
        open_pipe = None
        for x in range(len(pipe_map[y])):
            if pipe_map[y][x] == 1:
                if b_map[y][x] in '|' or (open_pipe == 'F' and b_map[y][x] == 'J') or (open_pipe == 'L' and b_map[y][x] == '7'):
                    inner = not inner
                if b_map[y][x] in "FL":
                    open_pipe = b_map[y][x]
            else:
                count += inner
    return count

def solve(b_map:list[list[str]]):
    pipe_map = {
        ((0,1),(+1,0)) : "F",
        ((0,-1),(+1,0)) : "7",
        ((0,-1),(0,+1)) : "-",
        ((-1,0),(+1,0)) : "|",
        ((-1,0),(0,-1)) : "J",
        ((-1,0),(0,+1)) : "L"
    }
    res = 0
    max_d_map = []
    start_y, start_x = get_start_point(b_map)

    b_map[start_y][start_x] = "#"
    start_dir = (0,0)
    for i, shift in enumerate([(1,0), (-1,0), (0,1), (0,-1)]):
        d_map = distance_map(b_map, start_y+shift[0], start_x+shift[1])
        cur_res = (max(map(max, d_map)))
        if res < cur_res:
            res = cur_res
            max_d_map = d_map
            start_dir = shift
    end = (0,0)
    for y in range(len(max_d_map)):
        for x in range(len(max_d_map[0])):
            if max_d_map[y][x] == res:
                end = (y,x)
    max_d_map[start_y][start_x] = 1
    pipe = restore_path(end, max_d_map, b_map)
    end_dir = (end[0]-start_y, end[1]-start_x)
    start_point = pipe_map.get((start_dir, end_dir), pipe_map.get((end_dir, start_dir)))
    b_map[start_y][start_x] = start_point
    print(start_point)
    res = count_inner(pipe, b_map)
    return res

        
def main():
    # input = open(r"./2023/10/input_second_test.txt")
    input = open(r"./2023/10/input_first.txt")
    input_lines = parse_input(input.readlines())
    b_map = add_borders(input_lines)
    # print(b_map)
    res = solve(b_map)
    print(res)

main()