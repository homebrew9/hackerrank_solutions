#!/bin/python

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    avb_sum = 0
    for i in ar:
        avb_sum += i
    return avb_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(long, raw_input().rstrip().split())

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

