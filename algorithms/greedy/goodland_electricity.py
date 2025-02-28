#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    # Write your code here
    prev, curr = -2*k, -k
    res = 0
    for i, v in enumerate(arr):
        if i - curr >= 2*k:
            return -1
        if v == 1:
            if i - prev >= 2*k:
                prev = curr
                res += 1
            curr = i
    return res

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    first_multiple_input = input().rstrip().split()
#    n = int(first_multiple_input[0])
#    k = int(first_multiple_input[1])
#    arr = list(map(int, input().rstrip().split()))
#    result = pylons(k, arr)
#    fptr.write(str(result) + '\n')
#    fptr.close()

# Main section
for k, arr in [
                 (3, [0,1,1,1,0,0,0]),
                 (2, [0,1,1,1,1,0]),
                 (2, [1,1,0,0,0,0,0,1]),
                 (3, [0,1,0,0,0,1,1,1,1,1]),
              ]:
    print(f'k, arr = {k}, {arr}')
    r = pylons(k, arr)
    print(f'r = {r}')
    print('========================')

