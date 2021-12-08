import numpy as np
from typing import List
    
def part1(lines: List[str]):
    state = np.asarray([int(n) for n in lines[0].split(",")])

    timer = np.zeros((9,), dtype=int)
    for fish in state:
        timer[fish] += 1

    for _ in range(80):
        new_fish = timer[0]
        timer[:-1] = timer[1:]

        timer[6] += new_fish
        timer[8] = new_fish

    return np.sum(timer)

def part2(lines: List[str]):
    state = np.asarray([int(n) for n in lines[0].split(",")])

    timer = np.zeros((9,), dtype=int)
    for fish in state:
        timer[fish] += 1

    for _ in range(256):
        new_fish = timer[0]
        timer[:-1] = timer[1:]

        timer[6] += new_fish
        timer[8] = new_fish

    return np.sum(timer)