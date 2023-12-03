from functools import reduce

def add_borders(a) -> list[list[str]]:
    n = len(a)
    m = len(a[0])
    res = [['.' for x in range(m+2)] for y in range(n+2)]
    for y in range(n):
        for x in range(m):
            res[y+1][x+1] = a[y][x]
    return res

def gears_near(a:list[list[str]], y:int, x:int) -> list[str]:
    nearest_y = [0,0,-1,1,-1,-1,1,1]
    nearest_x = [-1,1,0,0,-1,1,-1,1]
    gears = []
    for i_y,i_x in zip(nearest_y,nearest_x):
        sym = a[y+i_y][x+i_x]
        if not sym.isdigit() and sym == "*":
            gears.append(f"{y+i_y}_{x+i_x}")
    return gears

def find_part_numbers(a: list[list[str]]) -> int:
    res = {}
    n = len(a)
    m = len(a[0])
    for i in range(1,n-1):
        num = 0
        gears = set()
        to_add = False
        for j in range(1, m-1):
            if a[i][j].isdigit():
                num = num*10 + int(a[i][j])
                new_gears = gears_near(a, i, j)
                to_add = to_add or len(new_gears)>0
                gears.update(new_gears)
            else:
                if to_add:
                    for gear in gears:
                        if gear not in res:
                            res[gear] = {num}
                        else:
                            res[gear].update([num])
                num = 0
                gears = set()
                to_add = False
            # print(a[i][j], end="")
        if to_add:
            for gear in gears:
                if gear not in res:
                    res[gear] = {num}
                else:
                    res[gear].update([num])
    #     print()
    print(res)
    res = {k: v for k, v in res.items() if len(v) > 1}
    print(res)
    res_s = 0
    for x in res.values():
        y = 1
        for xx in x:
            y *= xx
        res_s+=y
    return res_s


def main():
    # input = open(r"./2023/03/input_second_test.txt")
    input = open(r"./2023/03/input_first.txt")
    a = list(map(lambda x: [*x.strip()], input.readlines()))
    a = add_borders(a)
    print(find_part_numbers(a))

main()