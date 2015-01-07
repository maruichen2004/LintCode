class Solution:
    def digitCounts(self, k, n):
        res = 0
        for i in range(0, n+1):
            res += self.getCount(k, i)
        return res
        
    def getCount(self, k, n):
        res = 0
        if n == 0:
            return 1 if k == 0 else res
        while n > 0:
            last = n % 10
            if last == k: res += 1
            n /= 10
        return res
