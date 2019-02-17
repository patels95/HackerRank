#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    minAbsDiff = float('inf')
    for i, num in enumerate(arr):
        for j in range(i + 1, len(arr)):
            absDiff = abs(num - arr[j])
            print(absDiff)
            if absDiff < minAbsDiff:
                minAbsDiff = absDiff
    return minAbsDiff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
