# Problem: Merge Two Sorted Lists (LeetCode #21)
# Approach: Two-pointer merge (like merge sort step)
# Time Complexity: O(n+m)
# Space Complexity: O(1)
# Reflection: Learned how to merge sorted structures efficiently.

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
