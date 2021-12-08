from typing import List
    
def part1(lines: List[str]):
    x = 0
    y = 0

    for line in lines:
        start, amount = line.split(" ")
        if start == "forward":
            x += int(amount)
        elif start == "down":
            y += int(amount)
        elif start == "up":
            y -= int(amount)

    return x * y

def part2(lines: List[str]):
    x = 0
    y = 0
    aim = 0

    for line in lines:
        start, amount = line.split(" ")
        if start == "forward":
            x += int(amount)
            y += aim * int(amount)
        elif start == "down":
            aim += int(amount)
        elif start == "up":
            aim -= int(amount)

    return x * y