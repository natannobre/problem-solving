#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    s_arr = sorted(arr)
    
    min = s_arr[0] + s_arr[1] + s_arr[2] + s_arr[3]
    max = s_arr[1] + s_arr[2] + s_arr[3] + s_arr[4]

    print (f"{min} {max}")
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
