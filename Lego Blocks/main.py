"""
Source: https://rb.gy/hfqk1
Date: 2023/8/15
Skill:
Ref:
Runtime: 171 ms, faster than 97.57%
Memory Usage: 27.93 MB, less than 11.95%
Time complexity:
Space complexity:
Constraints:

"""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(H, W):
    mod = 10 ** 9 + 7
    row = [1, 1, 2, 4]
    for _ in range(4, W + 1):
        row.append(sum(row[-4:]) % mod)
    for i in range(len(row)):
        row[i] = pow(row[i], H, mod)

    unstable = [0, 0]
    for i in range(2, W + 1):
        num = 0
        for j in range(1, i):
            num += (row[j] - unstable[j]) * row[i - j]
        unstable.append(num % mod)
    return (row[W] - unstable[W]) % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
