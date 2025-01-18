#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    N = len(s)
    i, j = 0, 0
    res = 0
    while j < N:
        if s[j] != s[i]:
            res += j - i - 1
            i = j
        j += 1
    res += j - i - 1
    return res

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    q = int(input().strip())
#
#    for q_itr in range(q):
#        s = input()
#
#        result = alternatingCharacters(s)
#
#        fptr.write(str(result) + '\n')
#
#    fptr.close()

for s in [
            'AAAA',
            'BBBBB',
            'ABABABAB',
            'BABABA',
            'AAABBB',
         ]:
    print(f's = {s}')
    r = alternatingCharacters(s)
    print(f'r = {r}')
    print('==================')


