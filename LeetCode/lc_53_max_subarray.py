# LeetCode 53: Maximum Subarray
# Approach: Kadane’s Algorithm
# Time Complexity: O(n), Space Complexity: O(1)

class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum

# Example run
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
