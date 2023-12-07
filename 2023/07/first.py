
import re


def parse_input(lines: list[str]) -> list[tuple[str,int]]:
    res = []
    for line in lines:
        hand_bid = line.strip().split(" ")
        hand = hand_bid[0]
        bid = int(hand_bid[1])
        res.append((hand, bid))
    return res

def add_kind(hand: str) -> int:
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

def solve(input_map:list[tuple[str,int]]):
    def key_function(key):
        hand, kind, _  = key
        hand = hand.replace("A","A")\
            .replace("K", "B")\
            .replace("Q", "C")\
            .replace("J", "D")\
            .replace("T","E")
        hand = hand.replace("9", "F")\
            .replace("8", "G")\
            .replace("7", "H")\
            .replace("6", "I")\
            .replace("5", "J")\
            .replace("4", "K")\
            .replace("3", "L")\
            .replace("2", "M")
        return kind, hand
    to_sort = []
    for hand_bid in input_map:
        to_sort.append((hand_bid[0], add_kind(hand_bid[0]), hand_bid[1]))
    # to_sort.sort(key= lambda x: (x[1], x[0]), reverse=True)
    to_sort.sort(key= key_function, reverse=True)
    print(to_sort)
    res = 0
    for i, hand in enumerate(to_sort):
        res += hand[2] * (i+1)
    return res
        
def main():
    # input = open(r"./2023/07/input_first_test.txt")
    input = open(r"./2023/07/input_first.txt")
    input_map = parse_input(input.readlines())
    res = solve(input_map)
    print(res)

main()