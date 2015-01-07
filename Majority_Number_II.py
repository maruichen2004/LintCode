class Solution:
    def majorityNumber(self, nums):
        if len(nums) == 0: return 0
        candidate1, count1 = 0, 0
        candidate2, count2 = 0, 0
        for i in range(len(nums)):
            if count1 != 0 and candidate1 == nums[i]: count1 += 1
            elif count2 != 0 and candidate2 == nums[i]: count2 += 1
            elif count1 == 0:
                count1, candidate1 = 1, nums[i]
            elif count2 == 0:
                count2, candidate2 = 1, nums[i]
            else:
                count1, count2 = count1 - 1, count2 - 1
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1: count1 += 1
            elif num == candidate2: count2 += 1
        return candidate2 if count1 < count2 else candidate1
