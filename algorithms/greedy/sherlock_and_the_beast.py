#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Write your code here
    for five_count in range((n // 3) * 3, -1, -3):
        if (three_count := (n - five_count)) % 5 == 0:
            print('5' * five_count + '3' * three_count)
            return
    print('-1')

#if __name__ == '__main__':
#    t = int(input().strip())
#    for t_itr in range(t):
#        n = int(input().strip())
#        decentNumber(n)

# Main section
for n in [
            1,
            3,
            5,
            11,
            100,
            102,
         ]:
    print(f'n = {n}')
    r = decentNumber(n)
    print('========================')

