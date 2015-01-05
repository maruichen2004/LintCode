class Solution:
    def subarraySum(self, nums):
        map, sum = {}, 0
        map[0] = -1
        for i in range(len(nums)):
            sum += nums[i]
            if sum in map: return [map[sum]+1, i]
            map[sum] = i
        return []
