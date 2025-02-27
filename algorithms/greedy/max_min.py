#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    N = len(arr)
    arr.sort()
    res = 10**20
    for i in range(0, N-k+1):
        res = min(res, arr[i+k-1] - arr[i])
    return res

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    n = int(input().strip())
#    k = int(input().strip())
#    arr = []
#    for _ in range(n):
#        arr_item = int(input().strip())
#        arr.append(arr_item)
#    result = maxMin(k, arr)
#    fptr.write(str(result) + '\n')
#    fptr.close()

# Main section
for k, arr in [
                 (2, [1,4,7,2]),
                 (3, [10,100,300,200,1000,20,30]),
                 (4, [1,2,3,4,10,20,30,40,100,200]),
                 (2, [1,2,1,2,1]),
              ]:
    print(f'k, arr = {k}, {arr}')
    r = maxMin(k, arr)
    print(f'r = {r}')
    print('========================')

