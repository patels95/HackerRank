#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    minDeletions = 0
    currentChar = s[0]
    for i in range(1, len(s)):
        if s[i] == currentChar:
            minDeletions += 1
        else:
            currentChar = s[i]
    return minDeletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
