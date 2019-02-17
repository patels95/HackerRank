#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    numPairs = 0
    pairs = {}
    for x in ar:
        socksInPair = pairs.get(x)
        if socksInPair is None:
            pairs[x] = 1
        else:
            numPairs += 1
            pairs.pop(x)
    return numPairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()