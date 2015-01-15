class Solution:
    def kSum(self, A, k, target):
        if len(A) < k: return 0
        dp = [[0 for i in range(target+1)] for j in range(k+1)]
        for i in range(1, len(A)+1):
            for j in reversed(range(1, min(i, k)+1)):
                for t in reversed(range(A[i-1], target+1)):
                    if j == 1: dp[1][t] += 1 if A[i-1] == t else 0
                    else: dp[j][t] += dp[j-1][t-A[i-1]]
        return dp[k][target]
