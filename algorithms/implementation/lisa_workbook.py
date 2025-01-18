#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    special_problems = 0
    page_no = 0
    for i in range(0, len(arr)):
        print('Chapter    : %d' % (i+1))
        print('Problems   : %d' % (arr[i]))
        start_page = page_no + 1
        print('Start page : %d' % start_page)
        a = arr[i] // k
        b = arr[i] % k
        if b == 0:
            page_no += a
        else:
            page_no += a+1
        print('To page#   : %d' % page_no)
        iter = 1 
        for p in range(start_page, page_no+1):
            if iter == 1:
                min_prob = 1
            else:
                min_prob = max_prob+1
            max_prob = iter*k
            if iter*k > arr[i]:
                max_prob = arr[i]
            print('Page: [%2d], (Min->Max prob) = ([%2d]->[%2d])' % (p, min_prob, max_prob))
            if min_prob <= p and p <= max_prob:
                special_problems += 1
                print('\t\t\t\t\t\tSpecial problems = [%d]' % special_problems)
            iter += 1
        print('-'*100)

    return special_problems 

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #nk = input().split()
    #n = int(nk[0])
    #k = int(nk[1])
    #arr = list(map(int, input().rstrip().split()))

    n = 5
    k = 2
    arr = [4, 2, 6, 1, 10]

    result = workbook(n, k, arr)
    print('====> ', result)

    #fptr.write(str(result) + '\n')
    #fptr.close()

