class Solution:
    def medianII(self, nums):
        minHeap, maxHeap, res, median = [], [], [], 0
        for i in range(len(nums)):
            tmp = nums[i]
            if i & 1:
                if heapq.nsmallest(1, maxHeap)[0] < -tmp:
                    heapq.heappush(maxHeap, -tmp)
                    tmp = -heapq.nsmallest(1, maxHeap)[0]
                    heapq.heappop(maxHeap)
                heapq.heappush(minHeap, tmp)
            else:
                if len(minHeap) > 0 and heapq.nsmallest(1, minHeap)[0] < tmp:
                    heapq.heappush(minHeap, tmp)
                    tmp = heapq.nsmallest(1, minHeap)[0]
                    heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -tmp)
            res.append(-heapq.nsmallest(1, maxHeap)[0])
        return res
