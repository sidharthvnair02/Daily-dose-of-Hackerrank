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
    
    max_ele = max(arr)
    min_ele = min(arr)
    max_list = []
    min_list =[] 
    if max_ele != min_ele:
        for i in range(0,len(arr)):
            if arr[i] == min_ele:
                min_list.append(arr[i])
            elif arr[i] != max_ele and arr[i]!= min_ele:
                max_list.append(arr[i])
                min_list.append(arr[i])
            elif arr[i] == max_ele:
                max_list.append(arr[i])
    else:
        max_list,min_list =  arr[1:],arr[1:]
    sum_max = sum(max_list)
    sum_min = sum(min_list)
    print(f"{sum_min} {sum_max}")
    return None
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
