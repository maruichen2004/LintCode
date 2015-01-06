class Solution: 
    def binarySearch(self, nums, target):
        l, r, res = 0, len(nums) - 1, -1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > k: r = mid - 1
            elif nums[mid] == k: res, r = mid, mid - 1
            else: l = mid + 1
        return res
