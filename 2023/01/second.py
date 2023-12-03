str_to_number_map = {
    "":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

def get_correct_number(corrupted_number: str) -> int:
    ans = ''
    first_ind = len(corrupted_number)
    first = ''
    last_ind = -1
    last = ''    
    for str_number, number in str_to_number_map.items():
        for search_str in [str_number, number]:
            if search_str == "":
                continue
            first_found_ind = corrupted_number.find(search_str)
            if first_found_ind!=-1 and first_found_ind<=first_ind:
                first_ind = first_found_ind
                first = number
            last_found_ind = corrupted_number.rfind(search_str)
            if last_found_ind!=-1 and last_found_ind>=last_ind:
                last_ind = last_found_ind
                last = number
    return int(f"{first}{last}")

def convert_to_numbers(corrupted_number:str) -> str:
    original = corrupted_number
    first = {
        "ind" : len(corrupted_number),
        "number" : 'x'
    }
    last = {
        "ind" : -1,
        "number" : 'x'
    }
    for text_number, number in str_to_number_map.items():
        cur_first = corrupted_number.find(text_number)
        cur_last = corrupted_number.rfind(text_number)
        if cur_first!= -1 and cur_first < first["ind"]:
            first["ind"] = cur_first
            first["number"] = number
        if cur_last!= -1 and cur_last > last["ind"]:
            last["ind"] = cur_last
            last["number"] = number
    corrupted_number = corrupted_number[:first["ind"]] + first["number"] + corrupted_number[first["ind"]:]
    corrupted_number = corrupted_number[:last["ind"]] + last["number"] + corrupted_number[last["ind"]:]
    print(f"{original} -> {corrupted_number}")
    return corrupted_number

def main():
    input = open(r"./2023/01/input_first.txt")
    numbers = map(get_correct_number, input.readlines())
    print(sum(numbers))

main()