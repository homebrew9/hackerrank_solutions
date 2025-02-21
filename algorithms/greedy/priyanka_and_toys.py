#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
    # Write your code here
    w.sort()
    res = 1
    val = w[0]
    for i in range(1, len(w)):
        if w[i] > val + 4:
            res += 1
            val = w[i]
    return res

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    n = int(input().strip())
#    w = list(map(int, input().rstrip().split()))
#    result = toys(w)
#    fptr.write(str(result) + '\n')
#    fptr.close()

# Main section
for w in [
            [1,2,3,21,7,12,14,21],
            [127,130,105,148,148,146,100,130,142,107,111,142,123,109,113,111,110,115,126,104],
            [2,6,8,2,9,4,2,1,7,6,7,3,8,9,4,7,8,6,6,6,1,5,2,6,1,9,6,3,3,1,6,8,9,2,1,7,7,4,6,10,6,4,9,7,3,4,10,9,8,3],
         ]:
    print(f'w = {w}')
    r = toys(w)
    print(f'r = {r}')
    print('========================')

