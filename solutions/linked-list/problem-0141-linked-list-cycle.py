# Problem: 141. Linked List Cycle
# Pattern: fast and slow pointers
# Key idea: compare node objects themselves, not node values.
# Mistake: the while condition is only a safety guard for fast.next access.

from typing import Optional


# LeetCode provides this class definition.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional["ListNode"]) -> bool:
        slow = head
        fast = head

        # This loop only guarantees fast can safely move two steps.
        # Whether there is a cycle is judged after slow and fast move.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next
            fast = fast.next

            if fast == slow:
                return True

        return False

