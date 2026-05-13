# Problem: Search in Rotated Sorted Array (LeetCode #33)
# Approach: Modified Binary Search (check sorted half)
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Reflection: Strengthened binary search intuition by handling rotated arrays.

def searchRotated(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid+1
            else:
                right = mid-1
    return -1
