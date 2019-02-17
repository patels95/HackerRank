#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    result = 0
    numAInOriginalString = 0
    quotient = int(n / len(s))
    remainder = n % len(s)
    for l in s:
        if l == 'a':
            numAInOriginalString += 1
    result = numAInOriginalString * quotient
    for l in s[:remainder]:
        if l == 'a':
            result += 1
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
