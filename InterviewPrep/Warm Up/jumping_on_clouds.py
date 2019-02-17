#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    minJumps = 0
    position = 0
    for index, val in enumerate(c):
        if index >= position:
            if (c[index + 2] if (index + 2) < len(c) else 1) == 0:
                position = index + 2
                minJumps += 1
            elif (c[index + 1] if (index + 1) < len(c) else 1) == 0:
                position = index + 1
                minJumps += 1
    return minJumps
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()