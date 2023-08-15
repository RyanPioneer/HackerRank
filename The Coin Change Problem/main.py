"""
Source: https://rb.gy/as9ob
Date: 2023/8/15
Skill:
Ref:
Runtime: 38 ms, faster than 97.06%
Memory Usage: 16.3 MB, less than 77.98%
Time complexity:
Space complexity:
Constraints:

"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    c.sort()
    dp, sz = [0 for _ in range(n + 1)], len(c)
    dp[0] = 1
    for i in range(sz):
        for j in range(c[i], n + 1):
            dp[j] += dp[j - c[i]]
    return dp[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
