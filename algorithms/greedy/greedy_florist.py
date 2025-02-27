#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    N = len(c)
    c.sort(reverse=True)
    factor = 1
    res = 0
    for i in range(0, N, k):
        res += sum(c[i:i+k]) * factor
        factor += 1
    return res

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    nk = input().split()
#    n = int(nk[0])
#    k = int(nk[1])
#    c = list(map(int, input().rstrip().split()))
#    minimumCost = getMinimumCost(k, c)
#    fptr.write(str(minimumCost) + '\n')
#    fptr.close()

# Main section
for k, c in [
               (3, [1,2,3,4]),
               (3, [2,5,6]),
               (2, [2,5,6]),
               (3, [1,3,5,7,9]),
            ]:
    print(f'k, c = {k}, {c}')
    r = getMinimumCost(k, c)
    print(f'r = {r}')
    print('========================')

