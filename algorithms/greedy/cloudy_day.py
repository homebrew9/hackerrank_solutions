#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    towns = [[xi, pi, -1] for xi, pi in zip(x, p)]
    towns = sorted(towns)
    m = len(y)
    cloud_start = [[y[i]-r[i], i] for i in range(m)]
    cloud_end = [[y[i]+r[i], i] for i in range(m)]
    cloud_start = sorted(cloud_start)
    cloud_end = sorted(cloud_end)
    cloud_start_i = 0
    cloud_end_i = 0
    clouds = set()

    d = defaultdict(int)
    free = 0
    for town_i in range(len(towns)):
        town_x = towns[town_i][0]
        while cloud_start_i < len(cloud_start) and cloud_start[cloud_start_i][0] <= town_x:
            clouds.add(cloud_start[cloud_start_i][1])
            cloud_start_i += 1
        while cloud_end_i < len(cloud_end) and cloud_end[cloud_end_i][0] < town_x:
            clouds.remove(cloud_end[cloud_end_i][1])
            cloud_end_i += 1
        if len(clouds) == 1:
            towns[town_i][2] = list(clouds)[0]
            d[list(clouds)[0]] += towns[town_i][1]
        elif len(clouds) == 0:
            free += towns[town_i][1]
    return max(d.values(), default=0) + free

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    n = int(input().strip())
#    p = list(map(int, input().rstrip().split()))
#    x = list(map(int, input().rstrip().split()))
#    m = int(input().strip())
#    y = list(map(int, input().rstrip().split()))
#    r = list(map(int, input().rstrip().split()))
#    result = maximumPeople(p, x, y, r)
#    fptr.write(str(result) + '\n')
#    fptr.close()

# Main section
for p, x, y, r  in [
                      ([10,100], [5,100], [4], [1]),
                   ]:
    print(f'p = {p}')
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'r = {r}')
    r1 = maximumPeople(p, x, y, r)
    print(f'r1 = {r1}')
    print('========================')

