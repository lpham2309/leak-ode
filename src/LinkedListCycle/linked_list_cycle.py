"""
141. Linked List Cycle
Problem Link: https://leetcode.com/problems/linked-list-cycle/description/
"""

from typing import Optional
from src.models.ListNode import ListNode

class LinkedListCycle:
    @staticmethod
    def hasCycle(head: Optional[ListNode]) -> bool:
        node_tracker = dict()

        while head:
            if head not in node_tracker:
                node_tracker[head] = True
            else:
                return True
        return False