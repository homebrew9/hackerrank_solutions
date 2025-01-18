#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
#def squares(a, b):
#    square_count = 0
#    for i in range(a, b+1):
#        num = math.sqrt(i)
#        if num == int(num):
#            square_count += 1
#    return square_count

def squares(a, b):
    square_count = 0
    # Check if the ends are perfect squares, obtain their square roots
    start = math.sqrt(a)
    if start == int(start):
        square_count += 1
    start = int(start)
    if b > a:
        end = math.sqrt(b)
        if end == int(end):
            square_count += 1
        end = int(end)
        # Now iterate through the range of potential square roots
        for i in range(start+1, end+1):
            num = i*i
            if a < num and num < b:
                square_count += 1
    return square_count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        ab = input().split()
        a = int(ab[0])
        b = int(ab[1])
        result = squares(a, b)
        print('====> ', result)
        #fptr.write(str(result) + '\n')
    #fptr.close()


