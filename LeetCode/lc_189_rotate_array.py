# LeetCode 189: Rotate Array
# Approach: Reverse method
# Time Complexity: O(n), Space Complexity: O(1)

class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums

# Example run
print(Solution().rotate([1,2,3,4,5,6,7], 3))  # Output: [5,6,7,1,2,3,4]
