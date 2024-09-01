import unittest
from src.models.ListNode import ListNode
from LinkedListCycle import LinkedListCycle

class TestLinkedListCycle(unittest.TestCase):
    
    def test_linked_list_with_null_value(self):
        head = ListNode(None, None)
        linkedlist_cycle = LinkedListCycle()
        self.assertIsNotNone(linkedlist_cycle.hasCycle(head), False)

    def test_linked_list_with_correct_cycle(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(None, None))))
        linkedlist_cycle = LinkedListCycle()
        is_cycle = linkedlist_cycle.hasCycle(head)
        self.assertTrue(is_cycle)

    def test_linked_list_with_no_cycle(self):
        head = ListNode(1, None)
        linkedlist_cycle = LinkedListCycle()
        is_cycle = linkedlist_cycle.hasCycle(head)
        self.assertTrue(is_cycle)