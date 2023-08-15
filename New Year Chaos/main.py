"""
Source: https://rb.gy/nntrr
Date: 2023/8/14
Skill:
Ref:
Runtime: 
Memory Usage:
Time complexity:
Space complexity:
Constraints:

"""

import math, sys
from typing import List, Optional
from collections import defaultdict, Counter, deque
from heapq import heapify, heappush, heappop, nsmallest
import heapq
import functools
from bisect import bisect_left, bisect_right

# !/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


class BIT:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(self.nums)

    def update_delta(self, idx, delta):
        while idx < self.n:
            self.nums[idx] += delta
            idx += idx & (-idx)

    def query_sum(self, idx):
        res = 0
        while idx > 0:
            res += self.nums[idx]
            idx -= idx & (-idx)
        return res

    def query_range_sum(self, left, right):
        return self.query_sum(right) - self.query_sum(left - 1)


def minimumBribes(q):
    res, sz, flag = 0, len(q), False
    tree = BIT([0 for _ in range(sz + 1)])
    for i in range(sz - 1, -1, -1):
        cnt = tree.query_sum(q[i])
        if cnt > 2:
            flag = True
            break
        res += cnt
        tree.update_delta(q[i], 1)
    if flag:
        print("Too chaotic")
    else:
        print(res)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
