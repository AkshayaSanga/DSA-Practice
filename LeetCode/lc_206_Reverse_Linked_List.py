# Problem: Reverse Linked List (LeetCode #206)
# Approach: Iterative pointer reversal
# Time Complexity: O(n)
# Space Complexity: O(1)
# Reflection: Strengthened pointer manipulation skills.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

