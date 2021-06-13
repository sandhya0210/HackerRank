#!/bin/python3

import math
import os
import random
import re
import sys

def Arra(n,arr):
    arr.reverse()
    print(*arr,sep=" ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    Arra(n,arr)
