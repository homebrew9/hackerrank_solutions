#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    #bt_count = 0
    #for i, j, k in itertools.combinations(arr, 3):
    #    if j - i == d and k - j == d:
    #        bt_count += 1
    #return bt_count

    bt_count = 0
    num_dict = {i:1 for i in arr}
    print(len(num_dict))
    for i in range(0, len(arr)):
        if arr[i]+d in num_dict:
            if arr[i]+2*d in num_dict:
                #print('%d, %d, %d' % (arr[i], arr[i]+d, arr[i]+2*d))
                bt_count += 1
    return bt_count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    line_no = 1
    fh = open('beautiful_triplets_tc2_input.log', 'r')
    for line in fh:
        #print(len(line))
        if line_no == 1:
            nd = line.split()
            n = int(nd[0])
            d = int(nd[1])
            print('n = [%d], d = [%d]' % (n, d))
            line_no += 1
        else:
            arr = list(map(int, line.rstrip().split()))

    fh.close()

    #nd = input().split()
    #n = int(nd[0])
    #d = int(nd[1])
    #arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)
    print(result)

    #fptr.write(str(result) + '\n')
    #fptr.close()

