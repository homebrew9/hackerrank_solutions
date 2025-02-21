#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    # sorted(contests, key=lambda x: (-x[1], -x[0]))
    # [[8, 1], [5, 1], [2, 1], [1, 1], [10, 0], [5, 0]]
    arr = sorted(contests, key=lambda x: (-x[1], -x[0]))
    res = 0
    for luck, importance in arr:
        if importance == 1:
            if k == 0:
                res -= luck
            else:
                k -= 1
                res += luck
        else:
            res += luck
    return res

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    first_multiple_input = input().rstrip().split()
#    n = int(first_multiple_input[0])
#    k = int(first_multiple_input[1])
#    contests = []
#    for _ in range(n):
#        contests.append(list(map(int, input().rstrip().split())))
#    result = luckBalance(k, contests)
#    fptr.write(str(result) + '\n')
#    fptr.close()

# Main section
for k, contests in [
                      (2, [[5,1],[1,1],[4,0]]),
                      (1, [[5,1],[1,1],[4,0]]),
                      (3, [[5,1],[2,1],[1,1],[8,1],[10,0],[5,0]]),
                   ]:
    print(f'k, contests = {k}, {contests}')
    r = luckBalance(k, contests)
    print(f'r = {r}')
    print('=========================')

