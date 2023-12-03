
def add_borders(a) -> list[list[str]]:
    n = len(a)
    m = len(a[0])
    res = [['.' for x in range(m+2)] for y in range(n+2)]
    for y in range(n):
        for x in range(m):
            res[y+1][x+1] = a[y][x]
    return res

def is_symbol_near(a:list[list[str]], y:int, x:int) -> bool:
    nearest_y = [0,0,-1,1,-1,-1,1,1]
    nearest_x = [-1,1,0,0,-1,1,-1,1]
    for i_y,i_x in zip(nearest_y,nearest_x):
        sym = a[y+i_y][x+i_x]
        if not sym.isdigit() and sym != ".":
            return True
    return False

def find_part_numbers(a: list[list[str]]) -> int:
    res = []
    n = len(a)
    m = len(a[0])
    for i in range(1,n-1):
        num = 0
        to_add = False
        for j in range(1, m-1):
            if a[i][j].isdigit():
                num = num*10 + int(a[i][j])
                to_add = to_add or is_symbol_near(a, i, j)
            else:
                if to_add:
                    res.append(num)
                num = 0
                to_add = False
            # print(a[i][j], end="")
        if to_add:
            res.append(num)
    #     print()
    # print(res)
    return sum(res)


def main():
    # input = open(r"./2023/03/input_first_test.txt")
    input = open(r"./2023/03/input_first.txt")
    a = list(map(lambda x: [*x.strip()], input.readlines()))
    a = add_borders(a)
    print(find_part_numbers(a))

main()