#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    # Write your code here
    # hsh is a dictionary that stores the index for each value
    hsh = {v:i for i, v in enumerate(arr)}
    N = len(arr)
    # Intuition: If we have a reverse-sorted array of length N containing *ALL*
    # integers in the range [1, N], then the integer at index i must be N - i.
    for i in range(N):
        if arr[i] != N - i:
            idx = hsh[N - i]
            # Update the indices of arr[i] and arr[N - i]
            hsh[arr[i]] = idx
            hsh[N-i] = i
            # Swap elements at indices i and idx
            arr[i], arr[idx] = arr[idx], arr[i]
            k -= 1
            if k == 0:
                break
    return arr

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    first_multiple_input = input().rstrip().split()
#    n = int(first_multiple_input[0])
#    k = int(first_multiple_input[1])
#    arr = list(map(int, input().rstrip().split()))
#    result = largestPermutation(k, arr)
#    fptr.write(' '.join(map(str, result)))
#    fptr.write('\n')
#    fptr.close()

# Main section
for k, arr in [
                 (1, [4,2,3,5,1]),
                 (1, [2,1,3]),
                 (1, [2,1]),
                 (5, [13,3,15,6,4,8,9,17,19,11,5,12,16,18,20,7,1,10,2,14]),
              ]:
    print(f'k, arr = {k}, {arr}')
    r = largestPermutation(k, arr)
    print(f'r = {r}')
    print('========================')


