class Solution:
    def recoverRotatedSortedArray(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                self.reverse(nums, 0, i)
                self.reverse(nums, i+1, len(nums)-1)
                self.reverse(nums, 0, len(nums)-1)
                return
            
    def reverse(self, nums, start, end):
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
