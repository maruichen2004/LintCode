class Solution:
    def median(self, nums):
        n = len(nums)
        return self.medianHelper(nums, 0, n-1, n/2 + (n&1))
        
    def medianHelper(self, nums, start, end, k):
        i, j = start + 1, end
        while i <= j:
            while i <= j and nums[i] < nums[start]: i += 1
            while i <= j and nums[j] >= nums[start]: j -= 1
            if i < j: nums[i], nums[j] = nums[j], nums[i]
        nums[start], nums[j] = nums[j], nums[start]
        if j + 1 == k: return nums[j]
        elif j + 1 > k: return self.medianHelper(nums, start, j, k)
        else: return self.medianHelper(nums, j+1, end, k)
