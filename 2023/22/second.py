
from collections import defaultdict, deque
from functools import lru_cache
import heapq
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = []
    for line in lines:
        line = line.strip()
        parts = line.strip().split('~')
        res.append(tuple([tuple([int(x) for x in parts[0].split(',', 2)]), tuple([int(x) for x in parts[1].split(',', 2)])]))
    return res

def cross(a1,a2,b1,b2):
    aa1 = min(a1,a2)
    aa2 = max(a1,a2)
    bb1 = min(b1,b2)
    bb2 = max(b1,b2)
    return (aa1 <= bb1 <= aa2) or (aa1 <= bb2 <= aa2) or (bb1 <= aa1 <= bb2) or (bb1 <= aa2 <= bb2)

def fall(b:tuple[tuple[int,int,int], tuple[int,int,int]], p:list[list[tuple]], n:int):
    x1,y1,z1 = b[0]
    x2,y2,z2 = b[1]
    overlap = []
    while z1 > -1 and not overlap:
        for a in p[z1]:
            ax1,ax2 = a[0]
            ay1,ay2 = a[1]
            a_n = a[2]
            if cross(ax1, ax2, x1, x2) and cross(ay1, ay2, y1, y2):
                overlap.append(a_n)
        if not overlap:
            z1 -= 1
            z2 -= 1
    z1 += 1
    z2 += 1
    for iz in range(z1, z2+1):
        p[iz].append(tuple([tuple([x1,x2]), tuple([y1,y2]), n]))
    return (overlap, z1)

def fall_without(m: list[tuple[tuple[int,int,int]]], ignore:int, pos:list[list[tuple]], new_z_pos:dict[int,int], s_on:dict[int, list[int]], s_below:dict[int, list[int]]):
    b_to_fall= set()
    for i in range(len(m)):
        if i == ignore:
            continue
        brick = m[i]
        z_pos = new_z_pos[i] -1
        x1,y1,_ = brick[0]
        x2,y2,_ = brick[1]
        overlap = False
        while z_pos>=0 and not overlap:
            for a in pos[z_pos]:
                ax1,ax2 = a[0]
                ay1,ay2 = a[1]
                a_n = a[2]
                if cross(ax1, ax2, x1, x2) and cross(ay1, ay2, y1, y2) and a_n != ignore:
                    overlap = True
            if not overlap:
                z_pos -= 1
        if abs(z_pos - new_z_pos[i]) > 1:
            b_to_fall.add(i)
    
    q = deque(b_to_fall)
    while q:
        cur = q.popleft()
        if all([x == ignore or x in b_to_fall for x in s_on[cur]]):
            b_to_fall.add(cur)
            for x in s_below[cur]:
                if x != ignore and x not in q and x not in b_to_fall:
                    q.append(x)
    return b_to_fall


def solve(m: list[tuple[tuple[int,int,int], tuple[int,int,int]]]):
    for i in range(len(m)):
        x = m[i]
        if x[0][2] > x[1][2]:
            m[i] = tuple([x[1],x[0]])
    m.sort(key=lambda x: (min(x[0][2], x[0][2]), min(x[0][0],x[1][0]), min(x[0][1], x[1][1])))
    max_z = max([max(b[0][2], b[1][2]) for b in m]) + 1
    pos = [[] for iz in range(max_z)]
    s_on = defaultdict(set)
    s_below = defaultdict(set)
    new_z_pos = {}
    for i, brick in enumerate(m):
        rel, new_z = fall(brick, pos, i)
        new_z_pos[i] = new_z
        for ii in rel:
            s_on[i].add(ii)
            s_below[ii].add(i)
        print(f"brick: {i}, fall on {rel}")

    res = 0
    for ignore in range(len(m)):
        b_to_fall = fall_without(m, ignore, pos, new_z_pos, s_on, s_below)
        res += len(b_to_fall)
    return res

def main():
    # input = open(r"./2023/22/input_first_test.txt")
    input = open(r"./2023/22/input_first.txt")
    m = parse_input(input.readlines())
    res = solve(m)
    print(res)

main()