#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    #print(f'==> s = {s}')
    N = len(s)
    if s.startswith('0') or N == 1:
        print('NO')
        return
    res = ''
    for i in range(1, N):
        res = s[:i]
        j = i
        next_num = str(int(res) + 1)
        while j < N and s[j:].find(next_num) == 0:
            j += len(next_num)
            next_num = str(int(next_num) + 1)
        if j >= N:
            print(f'YES {res}')
            break
    else:
        print('NO')

#if __name__ == '__main__':
#    q = int(input().strip())
#
#    for q_itr in range(q):
#        s = input()
#
#        separateNumbers(s)

for s in [
            '1234',
            '91011',
            '99100',
            '101103',
            '010203',
            '13',
            '1',
            '99910001001',
            '7891011',
            '9899100',
            '999100010001',
         ]:
    print(f's = {s}')
    r = separateNumbers(s)
    #print(f'r = {r}')
    print('==================')


