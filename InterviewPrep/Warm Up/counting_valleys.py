#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    altitude = 0
    inValley = False
    for step in s:
        if step == "U":
            altitude += 1
            if altitude == 0 and inValley == True:
                # end valley
                valleys += 1
        else:
            if altitude == 0:
                # start valley
                inValley = True
            altitude -= 1
    return valleys
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()