from typing import List
    
def part1(lines: List[str]):
    openings = ['(','{','[','<']
    closings = [')','}',']','>']

    points = {')':3, ']':57,'}':1197, '>':25137}
    cost = 0

    for line in lines:
        stack = []

        if line[0] not in openings:
            continue
        stack.append(line[0])

        for c in line[1:]:
            if len(stack) > 0 and c == closings[openings.index(stack[-1])]:
                del stack[-1]
            elif c not in openings:
                cost += points[c]
                break
            else:
                stack.append(c)

    return cost

def part2(lines: List[str]):
    openings = ['(','{','[','<']
    closings = [')','}',']','>']

    incomplete_lines = []
    for line in lines:
        stack = []

        if line[0] not in openings:
            continue
        stack.append(line[0])

        corupt = False
        for c in line[1:]:
            if len(stack) > 0 and c == closings[openings.index(stack[-1])]:
                del stack[-1]
            elif c not in openings:
                corupt = True
                break
            else:
                stack.append(c)
                
        if not corupt:
            incomplete_lines.append((line, stack))

    points = {')':1, ']':2,'}':3, '>':4}
    scores = []

    for line, stack in incomplete_lines:
        t_score = 0
        completion = [closings[openings.index(c)] for c in reversed(stack)]

        for c in completion:
            t_score = t_score*5 + points[c]
        scores.append(t_score)

    return sorted(scores)[len(scores) // 2]