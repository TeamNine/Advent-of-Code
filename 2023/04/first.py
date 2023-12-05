
def get_card_score(game_line: str) -> int:
    cards_and_numbers = game_line.split(":")
    game_ind = cards_and_numbers[0].split(" ")[1]
    win_and_mine = cards_and_numbers[1].split("|")
    win_num = [int(num.strip()) for num in win_and_mine[0].strip().split(" ") if num != '']
    my_num = [int(num.strip()) for num in win_and_mine[1].strip().split(" ") if num != '']
    win_count = sum([1 if x in win_num else 0 for x in my_num])
    return 0 if win_count == 0 else 2**(win_count-1)

def main():
    # input = open(r"./2023/04/input_first_test.txt")
    input = open(r"./2023/04/input_first.txt")
    game_results = map(get_card_score, input.readlines())
    print(sum(game_results))

main()