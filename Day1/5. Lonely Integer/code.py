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
    # Write your code here
    b = a
    counter=[]
    for i in a:
        count=0
        for j in b:
            if i==j:
                count+=1
            else: 
                pass
        counter.append(count)
    for i in range(len(counter)):
        if counter[i] == 1:
            return a[i]
        else:
            pass
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
