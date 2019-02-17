#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglassArr = []
    for rowIndex, r in enumerate(arr):
        for colIndex, c in enumerate(r):
            if isValidHourglassCenter(rowIndex, colIndex):
                hourglassTotal = arr[rowIndex - 1][colIndex - 1] + arr[rowIndex - 1][colIndex] + \
                    arr[rowIndex - 1][colIndex + 1] + c + arr[rowIndex + 1][colIndex - 1] + \
                    arr[rowIndex + 1][colIndex] + arr[rowIndex + 1][colIndex + 1]
                hourglassArr.append(hourglassTotal)
    return max(hourglassArr)


def isValidHourglassCenter(rowIndex, colIndex):
    return rowIndex != 0 and rowIndex != 5 and colIndex != 0 and colIndex != 5

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
