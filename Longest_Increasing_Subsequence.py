class Solution:
    def longestIncreasingSubsequence(self, nums):
        if len(nums) == 0: return 0
        dp = [1 for i in range(len(nums))]
        res = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] >= nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                res = max(res, dp[i])
        return res
