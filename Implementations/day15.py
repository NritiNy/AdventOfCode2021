import queue
import numpy as np
from typing import List
    
def part1(lines: List[str]):
    risklevels = np.asarray([[int(x) for x in line] for line in lines])

    m = dict()
    for y in range(risklevels.shape[0]):
        for x in range(risklevels.shape[1]):
            val =  0 if y == 0 and x == 0 else float("inf")
            m[(x,y)] = ((x, y), val)

    m[(0,0)] = ((0,0), 0)
    visited = set()

    while ((risklevels.shape[1] - 1, risklevels.shape[0] - 1) not in visited):
        vertexSet = sorted(m.values(), key=lambda x: x[1])
        vertex = vertexSet[0]
        while vertex[0] in visited:
            vertexSet = vertexSet[1:]
            vertex = vertexSet[0]

        pos, val = vertex
        visited.add(pos)
        if pos != (risklevels.shape[1] - 1, risklevels.shape[0] - 1):
            m.pop(pos)
        
        adjacent = [(pos[0]-1, pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1)]
        adjacent = [m[p] for p in adjacent if m.get(p) is not None]

        for v in adjacent:
            if v[0] in visited:
                continue

            m[v[0]] = (v[0], min(val + risklevels[v[0][1], v[0][0]], v[1]))


    return m[(risklevels.shape[1] - 1, risklevels.shape[0] - 1)][1]

def part2(lines: List[str]):
    risklevels = np.asarray([[int(x) for x in line] for line in lines])

    y, x = risklevels.shape
    extended = np.tile(risklevels, (5, 5))

    for i in range(5):
        for j in range(5):
            if i == 0 and j == 0:
                continue
            s = (extended[i*y:(i+1)*y, j*x: (j+1)*x] + i + j) % 9
            s[np.where(s == 0)] = 9
            extended[i*y:(i+1)*y, j*x: (j+1)*x] = s

    risklevels = extended

    m = dict()
    for y in range(risklevels.shape[0]):
        for x in range(risklevels.shape[1]):
            m[(x,y)] = ((x,y), float("inf"))
    
    
    m[(0,0)] = ((0,0), 0)
    visited = set()

    while ((risklevels.shape[1] - 1, risklevels.shape[0] - 1) not in visited):
        vertexSet = sorted(m.values(), key=lambda x: x[1])
        vertex = vertexSet[0]
        while vertex[0] in visited:
            vertexSet = vertexSet[1:]
            vertex = vertexSet[0]

        pos, val = vertex
        visited.add(pos)
        if pos != (risklevels.shape[1] - 1, risklevels.shape[0] - 1):
            m.pop(pos)
        
        adjacent = [(pos[0]-1, pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1)]
        adjacent = [m[p] for p in adjacent if m.get(p) is not None]

        for v in adjacent:
            if v[0] in visited:
                continue

            m[v[0]] = (v[0], min(val + risklevels[v[0][1], v[0][0]], v[1]))

    return m[(risklevels.shape[1] - 1, risklevels.shape[0] - 1)][1]