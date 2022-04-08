#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    positive_numbers = 0
    negative_numbers = 0
    zeros = 0
    
    for num in arr:
        if num > 0:
            positive_numbers += 1
        elif num == 0:
            zeros += 1
        else:
            negative_numbers += 1
    
    print ('%.6f'%(positive_numbers/n))
    print ('%.6f'%(negative_numbers/n))
    print ('%.6f'%(zeros/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
