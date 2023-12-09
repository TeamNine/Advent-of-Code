
import re


def parse_input(lines: list[str]) -> list[tuple[str,int]]:
    navigation = lines[0].strip()
    navigation_map = {}
    for line in lines[2:]:
        if found:=re.match(r"^(?P<from>.*?) = \((?P<L>.*?), (?P<R>.*?)\)$", line.strip()):
            navigation_map[found.group("from")] =  (found.group("L"), found.group("R"))
    return navigation, navigation_map
    s_key = sorted(hand)
    pairs = {}
    for ch in s_key:
        if ch not in pairs:
            pairs[ch] = 1
        else:
            pairs[ch] += 1
    pairs_count = sorted(pairs.values(), reverse=True)
    if pairs_count[0] == 5:
        return 1
    if pairs_count[0] == 4:
        return 2
    if len(pairs_count) == 2 and pairs_count[0] == 3 and pairs_count[1] == 2:
        return 3
    if pairs_count[0] == 3:
        return 4
    if len(pairs_count) > 2 and pairs_count[0] == 2 and pairs_count[1] == 2:
        return 5
    if len(pairs_count) > 2 and pairs_count[0] == 2:
        return 6
    return 7

def solve(instruction, naviagation_map):
    res = 0
    cur = "AAA"
    cur_instruction = 0
    while cur != "ZZZ":
        cur = naviagation_map[cur][0] if instruction[cur_instruction] == "L" else naviagation_map[cur][1]
        cur_instruction += 1
        if cur_instruction == len(instruction):
            cur_instruction = 0
        res += 1
    return res
        
def main():
    # input = open(r"./2023/08/input_first_test.txt")
    input = open(r"./2023/08/input_first.txt")
    instruction, naviagation_map = parse_input(input.readlines())
    res = solve(instruction, naviagation_map)
    print(res)

main()