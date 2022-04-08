#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    s = re.split('(\d+)', s)
    s = s[1:]
    period = s[5]
    hh = int(s[0])
    mm = s[2]
    ss = s[4]
    
    if period == 'AM':
        if hh == 12:
            return(f'00:{mm}:{ss}')
        else:
            return(f'{hh:02d}:{mm}:{ss}')            
    elif period == 'PM':
        if hh == 12:
            return(f'12:{mm}:{ss}')
        else:
            hh += 12
            return(f'{hh}:{mm}:{ss}')
    

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
