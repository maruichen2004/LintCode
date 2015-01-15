class Solution:
    def longestCommonSubstring(self, A, B):
        if len(A) == 0 or len(B) == 0: return 0
        dp = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        res = -1
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]: dp[i][j] = dp[i-1][j-1] + 1
                else: dp[i][j] = 0
                res = max(res, dp[i][j])
        return res
