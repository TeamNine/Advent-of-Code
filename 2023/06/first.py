
import re


def parse_input(lines: list[str]) -> dict[int,int]:
    times = [int(x) for x in lines[0].split(":")[1].strip().split(" ") if x]
    distances = [int(x) for x in lines[1].split(":")[1].strip().split(" ") if x]
    return {k:v for k,v in zip(times, distances)}

def solve(input_map:dict[int,int]):
    res = 1
    for time,distance in input_map.items():
        win_count = 0
        for x in range(time):
            if (time - x) * x > distance:
                win_count += 1
        print(f"Win for {time} is {win_count}")
        res *= win_count
    return res
        
def main():
    # input = open(r"./2023/06/input_first_test.txt")
    input = open(r"./2023/06/input_first.txt")
    input_map = parse_input(input.readlines())
    res = solve(input_map)
    print(res)

main()