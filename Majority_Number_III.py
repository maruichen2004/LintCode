class Solution:
    def majorityNumber(self, nums, k):
        if len(nums) == 0: return 0
        map = {}
        map[nums[0]] = 1
        for i in range(1, len(nums)):
            if nums[i] in map:
                val = map[nums[i]] + 1
                if val == 0: del map[nums[i]]
                map[nums[i]] = val
            else:
                if len(map) < k - 1: map[nums[i]] = 1
                else:
                    keyList = []
                    for item in map:
                        map[item] -= 1
                        if map[item] == 0: keyList.append(item)
                    for key in keyList: del map[key]
        for item in map: map[item] = 0
        num, count = 0, 0
        for i in range(len(nums)):
            if nums[i] in map:
                val = map[nums[i]] + 1
                if val > count: num, count = nums[i], val
                map[nums[i]] = val
        return num
