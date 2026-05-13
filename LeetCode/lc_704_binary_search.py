# Problem: Binary Search (LeetCode #704)
# Approach: Iterative Binary Search (while loop)
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Reflection: Practiced iterative binary search, improved recursion/iteration intuition.

def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1
