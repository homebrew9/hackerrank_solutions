#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    pat1 = re.compile(r'([a-z]+)|([A-Z][a-z]*)')
    arr = pat1.findall(s)
    for x, y in arr:
        if x == '':
            print(y)
        else:
            print(x)
    return len(arr)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = camelcase(s)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()

