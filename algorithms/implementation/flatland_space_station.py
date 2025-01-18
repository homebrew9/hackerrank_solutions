#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    min_index = 0
    max_index = n - 1
    size = len(c)
    c.sort()
    max_dist = 0
    if (c[0] - min_index) > max_dist:
        max_dist = c[0] - min_index
        print('==> 1: ', max_dist)
    if (max_index - c[size-1]) > max_dist:
        max_dist = max_index - c[size-1]
        print('==> 2: ', max_dist)
    for i in range(0, size-1):
        dist = ((c[i+1] - c[i]) // 2)
        if dist > max_dist:
            max_dist = dist
            print('==> 3: ', max_dist)
    return max_dist

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)
    print('====> ', result)
    #fptr.write(str(result) + '\n')
    #fptr.close()

