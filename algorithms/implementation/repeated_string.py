#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    strlen = len(s)
    if n < strlen:
        acount_in_substr = len(re.sub(r'[^a]', r'', s[0:n]))
        acount_total = acount_in_substr
    else:
        p = n // strlen
        q = n % strlen
        acount_in_substr = len(re.sub(r'[^a]', r'', s[0:q]))
        acount_in_str = len(re.sub(r'[^a]', r'', s))
        acount_total = p * acount_in_str + acount_in_substr
    return acount_total

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()

