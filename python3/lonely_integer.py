#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    sa = sorted(a)
    stack = []
    
    for num in sa:
        if not stack:
            stack.append(num)
        elif stack[len(stack)-1] == num:
            stack.pop()
        else:
            stack.append(num)
    
    return stack[0]

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
