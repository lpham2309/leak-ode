import unittest
from models.ListNode import ListNode
import LinkedListCycle

class TestLinkedListCycle(unittest.TestCase):
    
    def test_linked_list_with_null_value(self):
        head = ListNode(None, None)
        self.assertIsNotNone(LinkedListCycle.hasCycle(head), False)

    def test_linked_list_with_correct_cycle(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(None, None))))
        is_cycle = LinkedListCycle.hasCycle(head)
        self.assertTrue(is_cycle)

    def test_linked_list_with_no_cycle(self):
        head = ListNode(1, None)
        is_cycle = LinkedListCycle.hasCycle(head)
        self.assertFalse(is_cycle)