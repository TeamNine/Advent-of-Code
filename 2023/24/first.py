
from collections import defaultdict, deque
from functools import lru_cache
import heapq
import math
import re

EPS = 1e-9
class Point:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __lt__(self, other):
        return self.x < other.x-1e-9 or abs(self.x - other.x) < 1e-9 and self.y < other.y - 1e-9

    def __str__(self) -> str:
        return f"x:{self.x},y:{self.y},z:{self.z}"
    
    def __repr__(self) -> str:
        return str(self)

class Line:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def dist(self, p:Point):
        return self.a * p.x + self.b * p.y + self.c

def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        parts = line.strip().split('@')
        pos = tuple(map(int, parts[0].split(', ', 2)))
        v = tuple(map(int, parts[1].split(', ', 2)))
        res.append((pos, v))
    return res

def make_line(data: tuple[tuple[int,int,int], tuple[int,int,int]]):
    def norm(a:int, b:int, c:int):
        z = math.sqrt(a*a + b*b)
        if abs(z) > 1e-9:
            return (a/z, b/z, c/z)
        return (a, b, c)
    pos, v = data
    x, y, z = pos
    vx, vy, vz = v
    ax = x
    ay = y
    az = z
    bx = x + vx
    by = y + vy
    bz = z + vz
    a = ay - by
    b = bx - ax
    c = - a * ax - b * ay
    return Line(*norm(a,b,c))

def det (a,b,c,d):
    return a*d-b*c
    
def intersect(m:Line, n:Line):
    zn = det (m.a, m.b, n.a, n.b);
    if (abs (zn) < EPS):
        return (False, None)
    x = - det (m.c, m.b, n.c, n.b) / zn
    y = - det (m.a, m.c, n.a, n.c) / zn
    return (True, Point(x,y,0)) 
 
def parallel(m:Line, n:Line):
    return abs (det (m.a, m.b, n.a, n.b)) < EPS
 
def equivalent(m:Line, n:Line):
	return abs (det (m.a, m.b, n.a, n.b)) < EPS \
    and abs (det (m.a, m.c, n.a, n.c)) < EPS \
    and abs (det (m.b, m.c, n.b, n.c)) < EPS


def solve(a:list[tuple[tuple[int,int,int], tuple[int,int,int]]], start:int, end:int):
    res = 0
    lines = [make_line(x) for x in a]
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            if not parallel(lines[i], lines[j]) and not equivalent(lines[i], lines[j]):
                inter, point = intersect(lines[i], lines[j])
                print(f"line {i=} and {j=}: {inter=}, {point=}")
                if inter:
                    if start-EPS<=point.x<=end+EPS and start-EPS<=point.y<=end+EPS:
                        t_i = (point.x - a[i][0][0]) / a[i][1][0]
                        t_j = (point.x - a[j][0][0]) / a[j][1][0]
                        if (t_i>0) and (t_j>0):
                            res += 1
                            print("Yes")
            else:
                print(f"line {i=} and {j=}: NO")
    return res

def main():
    # input = open(r"./2023/24/input_first_test.txt")
    input = open(r"./2023/24/input_first.txt")
    m = parse_input(input.readlines())
    res = solve(m, 200000000000000, 400000000000000)
    print(res)

main()