# Problem: Detect Cycle in Linked List (LeetCode #141)
# Approach: Floyd’s Cycle Detection (slow + fast pointers)
# Time Complexity: O(n)
# Space Complexity: O(1)
# Reflection: Learned the “tortoise and hare” technique for cycle detection.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

