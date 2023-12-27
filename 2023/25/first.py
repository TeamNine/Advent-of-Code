
from collections import defaultdict, deque
from functools import lru_cache
import heapq
import math
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    res = {}
    for line in lines:
        parts = line.strip().split(':')
        res[parts[0]] = [x.strip() for x in parts[1].split(' ') if x.strip()]
    return res

def mincut(gg:dict[str, list[str]], q:set[str]):
    n = len(q)
    v = {k:[k] for k in q}
    best_cut = None
    best_cost = 1e9
    exist = {k:True for k in q}
    for ph in range(n-1):
        in_a = {k:False for k in q}
        w = {k:0 for k in q}
        prev = None
        for it in range(n-ph):
            sel = None
            for i in q:
                if exist[i] and not in_a[i] and (sel is None or w[i] > w[sel]):
                    sel = i
            if (it == n-ph-1):
                if (w[sel] < best_cost):
                    best_cost = w[sel]
                    best_cut = v[sel]
                v[prev].extend(v[sel])
                for i in q:
                    gg[prev][i] += gg[sel][i]
                    gg[i][prev] += gg[sel][i]
                exist[sel] = False
            else:
                in_a[sel] = True
                for i in q:
                    w[i] += gg[sel][i]
                prev = sel
    print(best_cut)
    print(best_cost)
    return len(best_cut)

def solve(d:dict[str, list[str]]):
    res = 0
    gg = defaultdict(dict)
    q = set()
    for k,v in d.items():
        for vv in v:
            gg[k][vv] = 1
            gg[vv][k] = 1
            q.add(vv)
            q.add(k)
    for k in gg.keys():
        for kk in gg.keys():
            if kk not in gg[k]:
                gg[k][kk] = 0
    cut_v = mincut(gg, q)
    return cut_v * (len(q)-cut_v)

def main():
    # input = open(r"./2023/25/input_first_test.txt")
    input = open(r"./2023/25/input_first.txt")
    data = parse_input(input.readlines())
    res = solve(data)
    print(res)

main()