import numpy as np
from typing import List
    
def part1(lines: List[str]):
    numbers = [int(n.strip()) for n in lines[0].split(",")]
    boards = []
    marked_boards = []

    while len(lines) >=5:
        board = np.zeros((5, 5))
        for i in range(2, 7):
            row = np.asarray([int(n.strip()) for n in lines[i].split()])
            board[i-2, :] = row
        boards.append(board)
        lines = lines[6:]

    for board in boards:
        marked_boards.append(np.zeros(board.shape))

    for number in numbers:
        for i, board in enumerate(boards):
            tmp = marked_boards[i]
            tmp[np.where(board == number)] += 1
            marked_boards[i] = tmp

            c = np.sum(marked_boards[i], 0)
            r = np.sum(marked_boards[i], 1)

            if np.any(r == 5) or np.any(c == 5):
                s = np.sum(boards[i][np.where(marked_boards[i] == 0)])
                return int(s * number)
    
    return None

def part2(lines: List[str]):
    numbers = [int(n.strip()) for n in lines[0].split(",")]
    boards = []
    marked_boards = []
    winning = []
    last_winner = (-1, 0)

    while len(lines) >=5:
        board = np.zeros((5, 5))
        for i in range(2, 7):
            row = np.asarray([int(n.strip()) for n in lines[i].split()])
            board[i-2, :] = row
        boards.append(board)
        lines = lines[6:]

    for board in boards:
        marked_boards.append(np.zeros(board.shape))

    for number in numbers:
        for i, board in enumerate(boards):
            if i in winning:
                continue

            tmp = marked_boards[i]
            tmp[np.where(board == number)] += 1
            marked_boards[i] = tmp

            c = np.sum(marked_boards[i], 0)
            r = np.sum(marked_boards[i], 1)

            if np.any(r == 5) or np.any(c == 5):
                s = np.sum(boards[i][np.where(marked_boards[i] == 0)])
                last_winner = (i, number)
                winning.append(i)
    
    s = np.sum(boards[last_winner[0]][np.where(marked_boards[last_winner[0]] == 0)])
    return int(s * last_winner[1])