import numpy as np
from typing import List
from scipy import ndimage
from functools import reduce
from skimage.measure import regionprops
    
def part1(lines: List[str]):
    heightmap = np.asarray([[int(x) for x in line] for line in lines])
    bool_heightmap = heightmap < 9

    labels, _ = ndimage.label(bool_heightmap)
    low_points = [p.min_intensity for p in regionprops(labels, heightmap)]

    return sum([x+1 for x in low_points])

def part2(lines: List[str]):
    heightmap = np.asarray([[int(x) for x in line] for line in lines])
    bool_heightmap = heightmap < 9

    labels, _ = ndimage.label(bool_heightmap)
    basin_sizes = [p.area for p in regionprops(labels)]

    return reduce(lambda x, y: x*y, sorted(basin_sizes)[-3:])