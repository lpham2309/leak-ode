"""
49. Group Anagrams
Problem Link: https://leetcode.com/problems/group-anagrams/description/
"""

import collections
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = collections.defaultdict(list)

    for word in strs:
        counter = [0 for i in range(26)]
        for w in word:
            counter[ord(w) - ord('a')] += 1
        res[tuple(counter)].append(word)
    return list(res.values())