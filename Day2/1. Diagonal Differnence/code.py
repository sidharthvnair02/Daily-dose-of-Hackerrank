#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    sum_left = 0
    right_to_left =[]
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                sum_left+= arr[i][j]
            else : 
                pass
        right_to_left.append(arr[i][n-1-i]) 
    sum_right= sum(right_to_left)    
    
    absolute_difference = abs(sum_left - sum_right)
    
    return absolute_difference
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
