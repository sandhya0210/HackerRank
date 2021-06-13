#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print (fact)# Write your code here

if __name__ == '__main__':

    n = int(input().strip())

    factorial(n)