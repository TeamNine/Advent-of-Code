import re

first_number_re = re.compile(r"^.*?(?P<first>\d).*$")
def get_correct_number(corrupted_number: str) -> int:
    ans = ''
    for x in [corrupted_number, corrupted_number[::-1]]:
        number_match = first_number_re.match(x.strip())
        if not number_match:
            raise Exception(f"Can not parse number from: {x}")
        ans += number_match.group('first')
    return int(ans)

def main():
    input = open(r"./2023/01/input_first.txt")
    numbers = map(get_correct_number, input.readlines())
    print(sum(numbers))

main()