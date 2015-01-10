class Solution:
    def subarraySumClosest(self, nums):
        if len(nums) == 0: return []
        sums = [(0, -1)]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            sums.append((sum, i))
        sums.sort(key=lambda x:x[0])
        MIN = abs(sums[0][0] - sums[1][0])
        start = min(sums[0][1], sums[1][1]) + 1
        end = max(sums[0][1], sums[1][1])
        for i in range(1, len(nums)):
            diff = abs(sums[i][0] - sums[i+1][0])
            if diff < MIN:
                MIN = diff
                start = min(sums[i][1], sums[i+1][1]) + 1
                end = max(sums[i][1], sums[i+1][1])
        return [start, end]
