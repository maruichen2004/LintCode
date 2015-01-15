class Solution:
    def backPackII(self, m, A, V):
        if len(A) == 0: return 0
        dp = [[0 for i in range(m+1)] for j in range(len(A)+1)]
        for i in range(1, len(A)+1):
            for j in range(m+1):
                dp[i][j] = dp[i-1][j]
                if j-A[i-1] >= 0 and dp[i][j] < dp[i-1][j-A[i-1]] + V[i-1]:
                    dp[i][j] = dp[i-1][j-A[i-1]] + V[i-1]
        return max(dp[len(A)])
