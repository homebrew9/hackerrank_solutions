#!python
# Version 3

import sys

def simpleArraySum(n, ar):
    # Complete this function
    if len(ar) != n:
        print("Error: array length does not match n")
        sys.exit(0)

    sum = 0
    for i in range(n):
        sum += ar[i]
    return sum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)

