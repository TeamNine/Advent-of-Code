
import re

def parse_input(lines: list[str]) -> tuple[list[int], dict[str,str], dict[str, dict[int,int]]]:
    seeds = list(map(lambda x: int(x), lines[0].split(":")[1].strip().split(" ")))
    map_name = ""
    transformation_maps = {}
    range_maps = {}
    for line in lines[2:]:
        if line.strip() == "":
            continue
        if found:=re.match(r"^(?P<from>.*?)-to-(?P<to>.*?) map:.*$", line.strip()):
            transformation_maps[found.group("from")] = found.group("to")
            map_name = f'{found.group("from")}_{found.group("to")}'
            range_maps[map_name] = {}
            continue
        destination_start,source_start, length = list(map(lambda x:int(x),line.strip().split(" ", 2)))
        range_maps[map_name][source_start] = [destination_start, length]
    return seeds, transformation_maps, range_maps

def transform_map(start:str, end:str, t_map:dict[str,str], r_map:dict[str, dict[int,int]]):
    def interval_key(interval):
        key_endpoint, key_is_start, _, _ = interval
        key_order = 0 if key_is_start else 1
        return key_endpoint, key_order
    rt_map = {v:k for k,v in t_map.items()}
    cur_pos = end
    final_ranges = []
    while(cur_pos != start):
        cur_map = f"{rt_map[cur_pos]}_{cur_pos}"
        new_ranges = []
        for s_start_range, dst_range in r_map[cur_map].items():
            start_range = dst_range[0]
            end_range = start_range+dst_range[1]-1
            new_ranges.append([[s_start_range,s_start_range+dst_range[1]-1],[start_range, end_range]])
        temp_ranges = []
        for cur_range in new_ranges:
            temp_ranges.append([cur_range[1][0], True, cur_range, False])
            temp_ranges.append([cur_range[1][1], False, cur_range, False])
        for cur_range in final_ranges:
            temp_ranges.append([cur_range[0][0], True, cur_range, True])
            temp_ranges.append([cur_range[0][1], False, cur_range, True])

        temp_ranges.sort(key=interval_key)
        temp_final_ranges = []
        cur_start = -1
        cur_refs_payload = []
        for point, is_start, ref_range, from_dest in temp_ranges:
            if is_start:
                if cur_start != -1 and point != cur_start and point-1>=cur_start and cur_refs_payload:
                    temp_final_ranges.append([cur_start, point-1, cur_refs_payload.copy()])
                cur_start = point
                cur_refs_payload.append((ref_range, from_dest))
            else:
                if cur_start != -1 and point >= cur_start and cur_refs_payload:
                    temp_final_ranges.append([cur_start, point, cur_refs_payload.copy()])
                cur_refs_payload.remove((ref_range, from_dest))
                cur_start = point+1
        new_final_range = []
        for temp_final_range in temp_final_ranges:
            i_start, i_end, i_payloads = temp_final_range
            new_ranges = []
            best_dest = []
            for i_payload in i_payloads:
                c_range, c_from_dest = i_payload
                if c_from_dest:
                    shift_s = i_start - c_range[0][0]
                    shift_e = i_end - c_range[0][1]
                    if not best_dest or best_dest[1][1]> c_range[1][0] + shift_s:
                        best_dest = [[i_start, i_end], [c_range[1][0] + shift_s, c_range[1][1] + shift_e]]
            for i_payload in i_payloads:
                c_range, c_from_dest = i_payload
                if not c_from_dest:
                    shift_s = i_start - c_range[1][0]
                    shift_e = i_end - c_range[1][1]
                    if best_dest:
                        new_ranges.append([[c_range[0][0] + shift_s, c_range[0][1] + shift_e], best_dest[1]])
                    else:
                        new_ranges.append([[c_range[0][0] + shift_s, c_range[0][1] + shift_e],[i_start, i_end]])
            if len(new_ranges) == 0 and best_dest:
                new_ranges.append(best_dest)
            new_final_range.extend(new_ranges)
        final_ranges = new_final_range
        cur_pos = rt_map[cur_pos]
    return final_ranges

def solve(seeds:list[int], shortcuts:list[list[list[int]]]):
    res = -1
    positions_to_check = set()
    for i, x in enumerate(seeds):
        if i%2==1:
            continue
        start_pos = x
        end_pos = x+seeds[i+1]-1
        positions_to_check.update([start_pos])
        for shortcut in shortcuts:
            start_short = shortcut[0][0]
            if (start_pos < start_short and start_short <= end_pos):
                positions_to_check.update([start_short])
    for num in positions_to_check:
        res_loc = -1
        for shortcut in shortcuts:
            if shortcut[0][0] <= num and shortcut[0][1] >= num:
                num_loc = num - shortcut[0][0] + shortcut[1][0]
                if res_loc == -1 or num_loc < res_loc:
                    res_loc = num_loc
        if res_loc == -1:
            res_loc = num
        if res == -1 or res > res_loc:
            res = res_loc
    return res
        
def main():
    # input = open(r"./2023/05/input_first_test.txt")
    input = open(r"./2023/05/input_first.txt")
    seeds,transformation_map,range_maps = parse_input(input.readlines())
    ranges = transform_map("seed", "location", transformation_map, range_maps)
    res = solve(seeds, ranges)
    print(res)

main()