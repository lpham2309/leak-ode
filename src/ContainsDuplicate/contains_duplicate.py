"""
217. Contains Duplicate
Problem Link: https://leetcode.com/problems/contains-duplicate/description/
"""

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    result = set()

    for val in nums:
        if val not in result:
            result.add(val)
        else:
            return False
    return True