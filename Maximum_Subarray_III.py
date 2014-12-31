class Solution:
    def maxKSubArrays(self, nums, k):
        sums = [[-sys.maxint for i in range(k+1)] for j in range(len(nums)+1)]
        for i in range(len(nums) + 1):
            sums[i][0] = 0
        for i in range(1, len(nums) + 1):
            for j in range(1, min(i, k) + 1):
                sums[i][j] = sums[i-1][j]
                tmp = 0
                for p in reversed(range(j, i+1)):
                    tmp = max(0, tmp) + nums[p-1]
                    sums[i][j] = max(sums[i][j], sums[p-1][j-1] + tmp)
        return sums[len(nums)][k]
