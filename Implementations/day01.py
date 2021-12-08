from typing import List
    
def part1(lines: List[str]):
    result = -1

    current_depth = 0
    for depth in [int(line) for line in lines]:
        if depth > current_depth:
            result += 1
        
        current_depth = depth

    return result

def part2(lines: List[str]):
    result = -1

    depths = [int(line) for line in lines]
    current_depth = 0

    for i in range(len(depths) - 2):
        depth = sum(depths[i:i+3])
        if depth > current_depth:
            result += 1
        
        current_depth = depth

    return result