#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    N = len(sticks)
    sticks.sort()
    res = list()
    for i in range(2, N):
        if sticks[i-2] + sticks[i-1] > sticks[i]:
            res.append([sticks[i-2], sticks[i-1], sticks[i]])
    if len(res) == 0:
        return [-1]
    arr = sorted(res, key=lambda x: (-x[2], -x[0]))
    return arr[0]

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    n = int(input().strip())
#    sticks = list(map(int, input().rstrip().split()))
#    result = maximumPerimeterTriangle(sticks)
#    fptr.write(' '.join(map(str, result)))
#    fptr.write('\n')
#    fptr.close()

# Main section
for sticks in [
                 [1,2,3,4,5,10],
                 [1,1,1,3,3],
                 [1,2,3],
                 [1,1,1,2,3,5],
              ]:
    print(f'sticks = {sticks}')
    r = maximumPerimeterTriangle(sticks)
    print(f'r = {r}')
    print('========================')

