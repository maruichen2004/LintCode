class Solution:
    def majorityNumber(self, nums):
        if len(nums) == 0: return 0
        majorityIdx, count = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[majorityIdx]: count += 1
            else: count -= 1
            if count == 0:
                majorityIdx, count = i, 1
        return nums[majorityIdx]
