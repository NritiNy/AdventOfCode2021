from typing import List
    
def part1(lines: List[str]):
    template = lines[0]
    rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in lines[2:]}

    for _ in range(10):
        update = ""
        for i in range(len(template) - 1):
            pair = template[i:i+2]
            if pair in rules.keys():
                update += pair[0] + rules[pair]
        update += template[-1]
        template = update

    amounts = [template.count(c) for c in set(template)]
    return max(amounts) - min(amounts)

def part2(lines: List[str]):
    template = lines[0]
    rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in lines[2:]}

    pairs = []
    for i in range(len(template) - 1):
        pairs.append(template[i:i+2])

    pair_counter = {p: 1 for p in pairs}

    for _ in range(40):
        new_pair_counter = {}
        for pair, value in list(pair_counter.items()):
            new_pairs = [pair[0] + rules[pair], rules[pair] + pair[1]]

            if pair not in new_pair_counter.keys():
                new_pair_counter[pair] = 0
            for n_pair in new_pairs:
                if n_pair not in new_pair_counter.keys():
                    new_pair_counter[n_pair] = 0
                new_pair_counter[n_pair] += value

        pair_counter = new_pair_counter

    char_counter = dict()
    for k, v in pair_counter.items():
        if k[0] not in char_counter.keys():
            char_counter[k[0]] = 0
        char_counter[k[0]] += v

    if template[-1] not in char_counter.keys():
        char_counter[template[-1]] = 0
    char_counter[template[-1]] += 1

    return max(char_counter.values()) - min(char_counter.values())