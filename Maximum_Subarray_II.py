class Solution:
    def maxTwoSubArrays(self, nums):    
        if len(nums) < 2: return 0
        left_maxes = [0 for i in range(len(nums))]
        right_maxes = [0 for i in range(len(nums))]
        left_maxes[0] = nums[0]
        for i in range(1, len(nums)):
            left_maxes[i] = max(left_maxes[i-1] + nums[i], nums[i])
        cur = left_maxes[0]
        for i in range(1, len(nums)):
            if left_maxes[i] < cur: left_maxes[i] = cur
            else: cur = left_maxes[i]
        right_maxes[-1] = nums[-1]
        for i in reversed(range(len(nums)-1)):
            right_maxes[i] = max(right_maxes[i+1] + nums[i], nums[i])
        cur = right_maxes[-1]
        for i in reversed(range(len(nums)-1)):
            if right_maxes[i] < cur: right_maxes[i] = cur
            else: cur = right_maxes[i]
        res = -sys.maxint
        for i in range(len(nums)-1):
            if left_maxes[i] + right_maxes[i+1] > res:
                res = left_maxes[i] + right_maxes[i+1]
        return res
