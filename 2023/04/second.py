
def get_card_score(game_line: str) -> int:
    cards_and_numbers = game_line.split(":")
    game_ind = cards_and_numbers[0].split(" ")[1]
    win_and_mine = cards_and_numbers[1].split("|")
    win_num = [int(num.strip()) for num in win_and_mine[0].strip().split(" ") if num != '']
    my_num = [int(num.strip()) for num in win_and_mine[1].strip().split(" ") if num != '']
    win_count = sum([1 if x in win_num else 0 for x in my_num])
    return win_count

def process_cards(cards_win_stat: list[int]) -> list:
    number_of_cards = [1 for x in range(len(cards_win_stat))]
    for cur_card_numb, cur_card in enumerate(cards_win_stat):
        for copies_card in range(cur_card_numb+1, cur_card_numb+1+cur_card):
            number_of_cards[copies_card] += (1*number_of_cards[cur_card_numb])
    return number_of_cards

def main():
    # input = open(r"./2023/04/input_second_test.txt")
    input = open(r"./2023/04/input_first.txt")
    card_results = list(map(get_card_score, input.readlines()))
    print(sum(process_cards(card_results)))

main()