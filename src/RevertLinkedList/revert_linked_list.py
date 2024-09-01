from typing import Optional
from src.models.ListNode import ListNode

class RevertLinkedList:
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev