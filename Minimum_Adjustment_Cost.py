class Solution:
    def MinAdjustmentCost(self, A, target):
        dp = [[1 << 31 for i in range(101)] for j in range(len(A)+1)]
        for j in xrange(101):
            dp[0][j] = 0
        for i in range(1, len(A)+1):
            for j in range(1, 101):
                for k in range(max(1, j-target), min(100, j+target)+1):
                    dp[i][j] = min(dp[i][j], dp[i-1][k]+abs(A[i-1]-j))
        res = 1 << 31
        for j in range(1, 101):
            res = min(res, dp[len(A)][j])
        return res
