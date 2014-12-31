class Solution:
    def maxDiffSubArrays(self, nums):
        maxLR = [nums[0] for i in range(len(nums))]
        maxRL = [nums[-1] for i in range(len(nums))]
        minLR = [nums[0] for i in range(len(nums))]
        minRL = [nums[-1] for i in range(len(nums))]
        prev = nums[0]
        for i in range(1, len(nums)):
            sum = nums[i] + prev if prev > 0 else nums[i]
            prev = sum
            maxLR[i] = max(sum, maxLR[i-1])
        prev = nums[0]
        for i in range(1, len(nums)):
            sum = nums[i] + prev if prev < 0 else nums[i]
            prev = sum
            minLR[i] = min(sum, minLR[i-1])
        prev = nums[-1]
        for i in reversed(range(len(nums) - 1)):
            sum = nums[i] + prev if prev > 0 else nums[i]
            prev = sum
            maxRL[i] = max(sum, maxRL[i+1])
        prev = nums[-1]
        for i in reversed(range(len(nums) - 1)):
            sum = nums[i] + prev if prev < 0 else nums[i]
            prev = sum
            minRL[i] = min(sum, minRL[i+1])
        diff = -sys.maxint
        for i in range(len(nums) - 1):
            diff = max(diff, abs(maxLR[i] - minRL[i+1]))
        for i in reversed(range(1, len(nums))):
            diff = max(diff, abs(maxRL[i] - minLR[i-1]))
        return diff
