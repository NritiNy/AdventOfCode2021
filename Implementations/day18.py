from typing import List

def add(left: bool, pair, number):
    if number is None: 
        return pair
    if isinstance(pair, int): 
        return pair + number

    if left:
        return [add(True, pair[0], number), pair[1]]
    else:
        return [pair[0], add(False, pair[1], number)]

def explode(pair, depth = 0):
    if isinstance(pair, int):
        return False, None, pair, None

    if depth == 4:
        return True, pair[0], 0, pair[1]

    left, right = pair
    changed, _l, left, _r = explode(left, depth+1)
    if changed:
        return True, _l, [left, add(True, right, _r)], None
    changed, _l, right, _r = explode(right, depth+1)
    if changed:
        return True, None, [add(False, left, _l), right], _r
    return False, None, pair, None

def split(pair):
    if isinstance(pair, int):
        if pair > 9:
            return True, (pair // 2, pair - (pair // 2))
        return False, pair
    
    left, right = pair
    changed, left = split(left)
    if changed:
        return True, [left, right]
    changed, right = split(right)
    return changed, [left, right]

def add_lines(left, right):
    pair = [left, right]
    while True:
        changed, _l, pair, _r = explode(pair)
        if changed:
            continue
        changed, pair = split(pair)
        if not changed:
            break
    return pair

def magnitude(pair):
    if isinstance(pair, int):
        return pair
    return 3 * magnitude(pair[0]) + 2 * magnitude(pair[1])

def part1(lines: List[str]):
    lines = list(map(eval, lines))

    first = lines[0]
    for line in lines[1:]:
        first = add_lines(first, line)

    return magnitude(first)

def part2(lines: List[str]):
    lines = list(map(eval, lines))

    max_magnitude = 0
    for i, line in enumerate(lines):
        for j, _line in enumerate(lines):
            if j == i:
                continue
            max_magnitude = max(max_magnitude, magnitude(add_lines(line, _line)))
    return max_magnitude