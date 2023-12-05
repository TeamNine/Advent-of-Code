
import re


def parse_input(lines: list[str]) -> tuple[list[int], dict[str,str], dict[str, dict[int,int]]]:
    seeds = list(map(lambda x: int(x), lines[0].split(":")[1].strip().split(" ")))
    
    map_name = ""
    r_map_name = ""
    transformation_maps = {}
    range_maps = {}
    for line in lines[2:]:
        if line.strip() == "":
            continue
        if found:=re.match(r"^(?P<from>.*?)-to-(?P<to>.*?) map:.*$", line.strip()):
            transformation_maps[found.group("from")] = found.group("to")
            map_name = f'{found.group("from")}_{found.group("to")}'
            r_map_name = f'{found.group("to")}_{found.group("from")}'
            range_maps[map_name] = {}
            range_maps[r_map_name] = {}
            continue
        destination_start,source_start, length = list(map(lambda x:int(x),line.strip().split(" ", 2)))
        range_maps[map_name][source_start] = [destination_start, length]
        # for x in range(length):
            # range_maps[map_name][source_start+x] = destination_start+x
            # range_maps[r_map_name][destination_start+x] = source_start+x
    return seeds, transformation_maps, range_maps

def solve(nums:list[int], start:str, end:str, t_map:dict[str,str], r_map:dict[str, dict[int,int]]):
    res = {}
    for num in nums:
        cur = start
        dest_num = num
        while (cur != end):
            map_name = f"{cur}_{t_map[cur]}"
            new_dst = dest_num
            for start_range, dst_range in r_map[f"{cur}_{t_map[cur]}"].items():
                if (dest_num >= start_range and dest_num <= start_range+dst_range[1]):
                    new_dst = dst_range[0] + dest_num-start_range
            # if dest_num in r_map[f"{cur}_{t_map[cur]}"]:
            #     dest_num = r_map[f"{cur}_{t_map[cur]}"][dest_num]
            dest_num=new_dst
            cur = t_map[cur]
        res[num] = dest_num
    return res
        
def main():
    # input = open(r"./2023/05/input_first_test.txt")
    input = open(r"./2023/05/input_first.txt")
    seeds,transformation_map,range_maps = parse_input(input.readlines())
    res = solve(seeds, "seed", "location", transformation_map,range_maps)
    print(res)
    print(min(res.values()))

main()