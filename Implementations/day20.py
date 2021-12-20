import numpy as np
import matplotlib.pyplot as plt
from typing import List
    
def part1(lines: List[str]):
    algorithm = lines[0]

    input_image = np.asarray([[0 if c == '.' else 1 for c in line] for line in lines[2:]], dtype=int)
    input_image = np.pad(input_image, 3, mode='constant', constant_values=0)
    
    for _ in range(2):
        padded = np.pad(input_image, 1, mode='edge')
        for y in range(1, input_image.shape[0] + 1):
            for x in range(1, input_image.shape[1] + 1):
                conv = padded[y-1:y+2,x-1:x+2]
                b = ""
                for i in range(3):
                    b += "".join(str(val) for val in conv[i])
                input_image[y-1, x-1] = 0 if algorithm[int(b, 2)] == '.' else 1
        input_image = np.pad(input_image, 3, mode='edge')

    return np.sum(input_image)

def part2(lines: List[str]):
    algorithm = lines[0]

    input_image = np.asarray([[0 if c == '.' else 1 for c in line] for line in lines[2:]], dtype=int)
    input_image = np.pad(input_image, 3, mode='constant', constant_values=0)
    
    for _ in range(50):
        padded = np.pad(input_image, 1, mode='edge')
        for y in range(1, input_image.shape[0] + 1):
            for x in range(1, input_image.shape[1] + 1):
                conv = padded[y-1:y+2,x-1:x+2]
                b = ""
                for i in range(3):
                    b += "".join(str(val) for val in conv[i])
                input_image[y-1, x-1] = 0 if algorithm[int(b, 2)] == '.' else 1
        input_image = np.pad(input_image, 3, mode='edge')

    return np.sum(input_image)