
import re


def parse_input(lines: list[str]) -> list[tuple[str,int]]:
    res = []
    for line in lines:
        res.append([int(x) for x in line.strip().split(' ') if x != ''])
    return res

def solve(input_lines:list[list[int]]):
    res = []
    for line in input_lines:
        line.reverse()
        print(f"{line=}")
        tmp = [line[0]]
        for i in range(1,len(line)):
            new_tmp = [line[i]]
            for j in range(len(tmp)):
                if (j == len(tmp)-1):
                    if not (tmp[j] == 0 and new_tmp[j] == 0):
                        new_tmp.append(new_tmp[j]-tmp[j])
                else:
                    new_tmp.append(new_tmp[j] - tmp[j])
            tmp = new_tmp
            print(f"\t {i=}: {tmp}")
        res.append(sum(tmp))
    return res
        
def main():
    # input = open(r"./2023/09/input_second_test.txt")
    input = open(r"./2023/09/input_first.txt")
    input_lines = parse_input(input.readlines())
    res = solve(input_lines)
    print(sum(res))

main()