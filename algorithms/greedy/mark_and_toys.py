#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    res = 0
    total = 0
    for p in sorted(prices):
        if total + p <= k:
            total += p
            res += 1
        else:
            break
    return res

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    first_multiple_input = input().rstrip().split()
#    n = int(first_multiple_input[0])
#    k = int(first_multiple_input[1])
#    prices = list(map(int, input().rstrip().split()))
#    result = maximumToys(prices, k)
#    fptr.write(str(result) + '\n')
#    fptr.close()

# Main section
for prices, k in [
                    ([1,2,3,4], 7),
                    ([1,12,5,111,200,1000,10], 50),
                 ]:
    print(f'prices, k = {prices}, {k}')
    r = maximumToys(prices, k)
    print(f'r = {r}')
    print('========================')

