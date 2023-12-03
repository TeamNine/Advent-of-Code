import re


def parse_game(game_line: str) -> int:
    available_blocks = {
        "red":12,
        "green": 13,
        "blue": 14
    }
    ind_and_games = game_line.split(":")
    game_ind = ind_and_games[0].split(" ")[1]
    for round in ind_and_games[1].split(";"):
        for color_and_num in round.split(","):
            num,color = color_and_num.strip().split(" ", 1)
            if available_blocks[color] < int(num):
                return 0
    return int(game_ind)


def main():
    input = open(r"./2023/02/input_first.txt")
    game_results = map(parse_game, input.readlines())
    print(sum(game_results))

main()