class Solution:
    def kSumII(self, A, k, target):
        res = []
        self.kSumHelper(A, k, target, [], 0, 0, len(A), res)
        return res
        
    def kSumHelper(self, A, k, target, cur, s, l, la, res):
        if l == k and s == target: res.append(list(cur))
        if not A or l >= k or la + l < k: return
        self.kSumHelper(A[1:], k, target, cur, s, l, la-1, res)
        self.kSumHelper(A[1:], k, target, cur + [A[0]], s + A[0], l+1, la-1, res)
