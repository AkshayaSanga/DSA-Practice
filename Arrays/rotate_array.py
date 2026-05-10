def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    return nums

# Example run
print(rotate([1,2,3,4,5,6,7], 3))  
# Output: [5,6,7,1,2,3,4]
