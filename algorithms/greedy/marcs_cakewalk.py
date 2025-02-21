#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    # Write your code here
    calorie.sort(reverse=True)
    res = 0
    factor = 1
    for c in calorie:
        res += factor * c
        factor *= 2
    return res

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    n = int(input().strip())
#    calorie = list(map(int, input().rstrip().split()))
#    result = marcsCakewalk(calorie)
#    fptr.write(str(result) + '\n')
#    fptr.close()

# Main section
for calorie in [
                  [1,3,2],
                  [7,4,9,6],
               ]:
    print(f'calorie = {calorie}')
    r = marcsCakewalk(calorie)
    print(f'r = {r}')
    print('=========================')

