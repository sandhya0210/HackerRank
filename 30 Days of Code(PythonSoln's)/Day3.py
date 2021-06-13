#!/bin/python3

import math
import os
import random
import re
import sys

def Fun():
    
    if N%2 != 0 :
        print("Weird")
    elif N in range(6,21):
        N%2 == 0
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    N = int(input().strip())
    Fun()
