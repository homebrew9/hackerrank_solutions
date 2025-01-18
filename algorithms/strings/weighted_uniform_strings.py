#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    arr = [0] * 26
    N = len(s)
    i, j = 0, 0
    while j < N:
        if s[j] != s[i]:
            #ch = s[i]
            ind = ord(s[i]) - 97
            span = j - i
            arr[ind] = max(arr[ind], span)
            i = j
        j += 1
    ind = ord(s[i]) - 97
    span = j - i
    arr[ind] = max(arr[ind], span)
    res = list()
    for q in queries:
        #found = False
        for i in range(26):
            if q % (i + 1) == 0 and arr[i] * (i+1) >= q:
                res.append('Yes')
                #found = True
                break
        else:
            res.append('No')
        #if not found:
        #    res.append('No')
    return res

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    s = input()
#
#    queries_count = int(input().strip())
#
#    queries = []
#
#    for _ in range(queries_count):
#        queries_item = int(input().strip())
#        queries.append(queries_item)
#
#    result = weightedUniformStrings(s, queries)
#
#    fptr.write('\n'.join(result))
#    fptr.write('\n')
#
#    fptr.close()
#

for s, queries in [
                     ('abccddde', [1,3,12,5,9,10]),
                     ('aaabbbbcccddd', [5,9,7,8,12,5]),
                  ]:
    print(f's, queries = {s}, {queries}')
    r = weightedUniformStrings(s, queries)
    print(f'r = {r}')
    print('==================')


