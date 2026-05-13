# Problem: Sort Colors (LeetCode #75)
# Approach: Dutch National Flag (three pointers)
# Time Complexity: O(n)
# Space Complexity: O(1)
# Reflection: Learned in-place sorting using low, mid, high pointers.

def sortColors(nums):
    low, mid, high = 0, 0, len(nums)-1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low+=1; mid+=1
        elif nums[mid] == 1:
            mid+=1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high-=1
