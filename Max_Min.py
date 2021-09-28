# Link: https://www.hackerrank.com/challenges/angry-children/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def maxMin(k, arr):
    # Write your code here
    k-=1
    arr.sort()
    return min(arr[i+k]-arr[i] for i in range(len(arr)-k))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
