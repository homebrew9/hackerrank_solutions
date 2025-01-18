#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    term_count = 0
    max_term_count = 1
    cumulative_sum = 0
    a.sort()
    for i in range(0, len(a)-1):
        term_count += 1
        cumulative_sum += a[i+1] - a[i]
        if cumulative_sum > 1:
            if term_count > max_term_count:
                max_term_count = term_count
            term_count = 0
            cumulative_sum = 0
    if cumulative_sum <= 1:
        if term_count + 1 > max_term_count:
            max_term_count = term_count + 1
    return max_term_count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #n = int(input().strip())
    #a = list(map(int, input().rstrip().split()))
    #result = pickingNumbers(a)
    #fptr.write(str(result) + '\n')
    #fptr.close()

    for a in [
                 [1, 1, 2, 2, 2, 3],
                 [4, 6, 5, 3, 3, 1],
                 [1, 1, 2, 2, 4, 4, 5, 5, 5],
                 [1, 1, 1, 1, 3, 3, 3, 3, 3, 7],
                 [1, 1, 1, 1, 3, 3, 3, 3, 3],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1],
                 [1, 9],
                 [9],
                 [1, 3, 5, 7, 9, 11, 13, 15, 17]
             ]:
        print(a)
        result = pickingNumbers(a)
        print(result)

