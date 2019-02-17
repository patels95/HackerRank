#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    flavors = {cost[i]: i + 1 for i in range(len(cost))}
    for index, c in enumerate(cost):
        val = money - c
        flavorID = flavors.get(val)
        if flavorID is not None and flavorID != (index + 1):
            print(str(min(flavorID, index + 1)) + " " + str(max(flavorID, index + 1)))
            break
        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
