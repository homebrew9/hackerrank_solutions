#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    def findPosition(ranked, p):
        left, right = 0, len(ranked)-1
        while left <= right:
            mid = (left + right) // 2
            if ranked[mid] == p:
                return mid
            elif ranked[mid] > p:
                left = mid + 1
            else:
                right = mid - 1
        return left
    hsh = dict()
    rank = 1
    hsh[0] = rank
    N = len(ranked)
    for i in range(1, N):
        if ranked[i] != ranked[i-1]:
            rank += 1
        hsh[i] = rank
    res = list()
    for p in player:
        ind = findPosition(ranked, p)
        if ind >= N:
            res.append(hsh[N-1]+1)
        else:
            res.append(hsh[ind])
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    for _ in range(N):

        ranked_count = int(input().strip())

        ranked = list(map(int, input().rstrip().split()))

        player_count = int(input().strip())

        player = list(map(int, input().rstrip().split()))

        result = climbingLeaderboard(ranked, player)

        fptr.write('\n'.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

