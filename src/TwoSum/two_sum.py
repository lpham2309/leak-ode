"""
1. Two Sum
Problem Link: https://leetcode.com/problems/two-sum/
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    res = {}
    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining not in res:
            res[nums[i]] = i
        else:
            return [res[remaining], i]
