#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    res = float('inf')
    for i in range(1, len(arr)):
        res = min(res, abs(arr[i] - arr[i-1]))
    return res

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    n = int(input().strip())
#    arr = list(map(int, input().rstrip().split()))
#    result = minimumAbsoluteDifference(arr)
#    fptr.write(str(result) + '\n')
#    fptr.close()

# Main section
for arr in [
              [3,-7,0],
              [-59,-36,-13,1,-53,-92,-2,-96,-54,75],
              [1,-3,71,68,17],
           ]:
    print(f'arr = {arr}')
    r = minimumAbsoluteDifference(arr)
    print(f'r = {r}')
    print('=========================')

