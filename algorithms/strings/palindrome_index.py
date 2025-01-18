#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    def is_palindrome(t):
        left, right = 0, len(t) - 1
        while left < right:
            if t[left] != t[right]:
                return False
            left += 1
            right -= 1
        return True
    if is_palindrome(s):
        return -1
    N = len(s)
    arr = list(s)
    i, j = 0, N - 1
    while i < j:
        if arr[i] != arr[j]:
            if is_palindrome(s[:i] + s[i+1:]):
                return i
            if is_palindrome(s[:j] + s[j+1:]):
                return j
        i += 1
        j -= 1
    return -1

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    q = int(input().strip())
#
#    for q_itr in range(q):
#        s = input()
#
#        result = palindromeIndex(s)
#
#        fptr.write(str(result) + '\n')
#
#    fptr.close()

for s in [
            'bcbc',
            'aaab',
            'baa',
            'aaa',
            'fvyqxqxynewuebtcuqdwyetyqqisappmunmnldmkttkmdlnmnumppasiqyteywdquctbeuwenyxqxqyvf',
            'mmbiefhflbeckaecprwfgmqlydfroxrblulpasumubqhhbvlqpixvvxipqlvbhqbumusaplulbrxorfdylqmgfwrpceakceblfhfeibmm',
            'fwcwcwcacwcwcf',
         ]:
    print(f's = {s}')
    r = palindromeIndex(s)
    print(f'r = {r}')
    print('=================')


