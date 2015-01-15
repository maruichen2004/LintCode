class Solution:
    def backPack(self, m, A):
        if len(A) == 0: return 0
        dp = [False for i in range(m + 1)]
        dp[0] = True
        for i in range(1, len(A) + 1):
            for j in reversed(range(m+1)):
                if j - A[i-1] >= 0 and dp[j-A[i-1]]:
                    dp[j] = dp[j-A[i-1]]
        for i in reversed(range(m+1)):
            if dp[i]: return i
        return 0
