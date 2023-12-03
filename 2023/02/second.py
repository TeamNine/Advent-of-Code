import re


def parse_game(game_line: str) -> int:
    available_blocks = {
        "red": -1,
        "green": -1,
        "blue": -1
    }
    ind_and_games = game_line.split(":")
    game_ind = ind_and_games[0].split(" ")[1]
    for round in ind_and_games[1].split(";"):
        for color_and_num in round.split(","):
            num,color = color_and_num.strip().split(" ", 1)
            available_blocks[color] = max(int(num),available_blocks[color])
    return available_blocks["blue"]*available_blocks["green"]*available_blocks["red"]


def main():
    input = open(r"./2023/02/input_first.txt")
    game_results = map(parse_game, input.readlines())
    print(sum(game_results))

main()