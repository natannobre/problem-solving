#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def reverse_row(l, matrix):
  matrix[l] = matrix[l][::-1]
  print("Reverse Row "+str(l))
  print(matrix)
  return matrix

def reverse_column(c, matrix):
  n = int(len(matrix)/2)
  for i in range (n):
      aux = matrix[i][c]
      matrix[i][c] = matrix[(2*n)-(i+1)][c]
      matrix[(2*n)-(i+1)][c] = aux
  print("Reverse Column "+str(c))
  print(matrix)
  return matrix
  
def flippingMatrix(matrix):
  n = int(len(matrix)/2)
  
  for c in range (len(matrix)):
    sum1 = 0
    sum2 = 0
    for i in range (n):
      sum1 += matrix[i][c]
      sum2 += matrix[(2*n)-(i+1)][c]

    print("For c = "+str(c)+", sum1 = "+str(sum1)+" e sum2 = "+str(sum2))
    if sum1 < sum2:
      reverse_column(c, matrix)
  
  for l in range (len(matrix)):
    sum1 = 0
    sum2 = 0
    for i in range (n):
      sum1 += matrix[l][i]
      sum2 += matrix[l][(2*n)-(i+1)]
    
    if sum1 < sum2:
          reverse_row(l, matrix)
  
  sum = 0
  for l in range(n):
    for c in range(n):
      sum += matrix[l][c]
  
  return sum


if __name__ == '__main__':
  q = int(input().strip())

  for q_itr in range(q):
    n = int(input().strip())

    matrix = []

    for _ in range(2 * n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = flippingMatrix(matrix)
    print(matrix)
    print (result)

# TEST CASE 1:
# 1
# 2
# 112 42 83 119
# 56 125 56 49
# 15 78 101 43
# 62 98 114 108