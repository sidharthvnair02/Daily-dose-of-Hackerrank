
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
    positive_count = 0 
    negative_count = 0 
    zeros = 0
    for i in range(len(arr)):
        if arr[i] > 0 :
            positive_count+= 1
        elif arr[i] < 0:
            negative_count+=1
        else :
            zeros+=1
    print(round(positive_count/len(arr),6))
    print(round(negative_count/len(arr),6))
    print(round(zeros/len(arr),6))
    return None
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
