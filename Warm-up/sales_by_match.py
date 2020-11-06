#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair = 0
    socks = {}
    
    for element in ar:
        if element not in socks.keys():
            socks[element] = 1
        else:
            socks[element] += 1
    
    for key in socks.keys():
        pair += socks[key]//2
        
    return pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
