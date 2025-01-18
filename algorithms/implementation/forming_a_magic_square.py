#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    def isMagicSquare(t):
        # Magic number for 3X3 matrix is 15
        magic_num = 15
        if sum(t[0:3]) != magic_num or sum(t[3:6]) != magic_num or sum(t[6:9]) != magic_num:
            return False
        if t[0]+t[3]+t[6] != magic_num or t[1]+t[4]+t[7] != magic_num or t[2]+t[5]+t[8] != magic_num:
            return False
        if t[0]+t[4]+t[8] != magic_num or t[2]+t[4]+t[6] != magic_num:
            return False
        return True
    def findCost(t1, t2):
        cost = 0
        for a, b in zip(t1, t2):
            cost += abs(a - b)
        return cost

    tpl = tuple()
    for r in range(3):
        for c in range(3):
            tpl += (s[r][c],)
    min_cost = float('inf')
    for t in permutations(range(10), 9):
        if isMagicSquare(t):
            cost = findCost(t, tpl)
            #print(f'\tMagic_Square, cost = {t}, {cost}')
            min_cost = min(min_cost, cost)
    #print(f'Min_cost = {min_cost}')
    return min_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().rstrip())

    for _ in range(N):
        s = []
        for _ in range(3):
            s.append(list(map(int, input().rstrip().split())))
        result = formingMagicSquare(s)
        fptr.write(str(result) + '\n')

    fptr.close()


