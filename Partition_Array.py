class Solution:
    def partitionArray(self, nums, k):
        if len(nums) == 0: return 0
        i, j = 0, len(nums) - 1
        while i < j:
            while i < len(nums) and nums[i] < k: i += 1
            while j >= 0 and nums[j] >= k: j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        return i
