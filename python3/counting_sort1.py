#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    n = len(arr)
    frequency_arr = [0]*100
    
    for i in range(n):
        frequency_arr[arr[i]] += 1

    return frequency_arr

if __name__ == '__main__':
  n = int(input().strip())

  arr = list(map(int, input().rstrip().split()))

  result = countingSort(arr)
