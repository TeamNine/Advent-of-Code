
from collections import defaultdict, deque
import heapq
import re

def parse_input(lines: list[str]) -> list[list[str]]:
    module_types = {
        'b': 0,
        '&': 1,
        '%': 2
    }
    cfg = {}
    connections = {}
    for line in lines:
        line = line.strip()
        parts = line.split(' -> ')
        m_type = module_types[parts[0][0]]
        m_name = parts[0] if m_type == 0 else parts[0][1:]
        dest = [p.strip() for p in parts[1].split(',')]
        connections[m_name] = dest
        cfg[m_name] = m_type
    return (connections, cfg)

def set_bit(val, index, bit):
    m = 1 << index
    return (val | m) if bit else (val & ~m)

def solve(connections: dict[str, list[str]], cfg: dict[str, list[str]]):
    inputs = defaultdict(dict)
    state = {}
    for start, dests in connections.items():
        state[start] = 0
        for dest in dests:
            inputs[dest][start] = len(inputs[dest])
    signals = deque([])
    res = {
        0:0,
        1:0
    }
    for i in range(1000):
        signals.append(("broadcaster", 0, "button"))
        while signals:
            cur_node, signal, from_node = signals.popleft()
            res[signal] += 1
            if cur_node not in state:
                continue
            old_state = state[cur_node]
            new_signal = 2
            if cfg[cur_node] == 0:
                new_signal = signal
            elif cfg[cur_node] == 1:
                state[cur_node] = set_bit(state[cur_node], inputs[cur_node][from_node], signal)
                new_signal = 1
                if state[cur_node] == (2 ** len(inputs[cur_node])-1):
                    new_signal = 0
            elif cfg[cur_node] == 2:
                if signal == 0:
                    state[cur_node] = 1 - state[cur_node]
                    new_signal = state[cur_node]
            # print(f"{from_node} - {signal} -> {cur_node} : {old_state} -> {state[cur_node]}")                
            if new_signal == 2:
                continue
            for dest in connections[cur_node]:
                signals.append((dest, new_signal, cur_node))
    return res[0]*res[1]

def main():
    # input = open(r"./2023/20/input_first_test.txt")
    input = open(r"./2023/20/input_first.txt")
    con, cfg = parse_input(input.readlines())
    res = solve(con, cfg)
    print(res)

main()