#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    # Generate the matrix
    blanks_present = False
    matrix = list()
    for line in grid:
        if line.find(' ') == -1:
            matrix.append([int(i) for i in line])
        else:
            blanks_present = True
            matrix.append([int(i) for i in line.split()])
    # Process matrix and set cavity depths
    n = len(matrix[0])
    for r in range(0, n):
        if r == 0 or r == n-1:
            continue
        for c in range(0, n):
            if c == 0 or c == n-1:
                continue
            if matrix[r][c] > max(matrix[r-1][c], matrix[r+1][c],
                                  matrix[r][c-1], matrix[r][c+1]):
                matrix[r][c] = -1
    # Process matrix again and repackage it into an array of strings
    cmap = list()
    for line in matrix:
        if blanks_present:
            cmap.append(' '.join(['X' if i == -1 else str(i) for i in line]))
        else:
            cmap.append(''.join(['X' if i == -1 else str(i) for i in line]))
    # And return the cavity map
    return cmap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(grid)
    #print(result)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()


