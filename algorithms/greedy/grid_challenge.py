#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    rows = len(grid)
    for i in range(rows):
        grid[i] = ''.join(sorted(grid[i]))
    cols = len(grid[0])
    for c in range(cols):
        for r in range(1, rows):
            if grid[r][c] < grid[r-1][c]:
                return 'NO'
    return 'YES'

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    t = int(input().strip())
#    for t_itr in range(t):
#        n = int(input().strip())
#        grid = []
#        for _ in range(n):
#            grid_item = input()
#            grid.append(grid_item)
#        result = gridChallenge(grid)
#        fptr.write(result + '\n')
#    fptr.close()

# Main section
for grid in [
               ['abc','ade','efg'],
               ['ebacd','fghij','olmkn','trpqs','xywuv'],
               ['abc','def','ghi','jkl','def'],
            ]:
    print(f'grid = {grid}')
    r = gridChallenge(grid)
    print(f'r = {r}')
    print('=========================')

