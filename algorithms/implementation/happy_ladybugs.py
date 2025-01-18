#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    empty_slot = re.compile(r'_')
    retval = 'YES'
    es_arr = empty_slot.findall(b)
    if len(es_arr) == 0:
        #print('No space in string...')
        # All ladybugs must be happy.
        # If every character from index 0 to n-2 is either
        # succeeded or preceded by the same character, then it
        # is a happy character.
        if len(b) == 1:
            retval = 'NO'
        else:
            for i in range(0, len(b)):
                if not ( (i < len(b)-1 and b[i] == b[i+1]) or b[i-1] == b[i] ):
                    retval = 'NO'
                    break
    else:
        #print('At least one space in string...')
        #print('No. of spaces in string: %d' % len(es_arr))
        # If all characters occur at least 2 times, then they can all be made happy.
        # Otherwise (i.e. if at least one character occurs only once), they cannot
        # be made happy.
        bug_dict = {}
        for ch in b:
            if ch != '_':
                if ch in bug_dict:
                    bug_dict[ch] += 1
                else:
                    bug_dict[ch] = 1
        for k in bug_dict:
            if bug_dict[k] == 1:
                retval = 'NO'
                break
    return retval

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    g = int(input())
    for g_itr in range(g):
        n = int(input())
        b = input()
        result = happyLadybugs(b)
        print(result)
        #fptr.write(result + '\n')
    #fptr.close()

