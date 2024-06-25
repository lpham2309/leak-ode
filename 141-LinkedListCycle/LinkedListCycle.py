from ListNode import ListNode 
from typing import Optional

class LinkedListCycle():
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_tracker = dict()

        while head:
            if head not in node_tracker:
                node_tracker[head] = True
            else:
                return True
        return False