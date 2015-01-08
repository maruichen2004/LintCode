class Solution:
    def productExcludeItself(self, A):
        if len(A) < 2: return []
        res = [1] * len(A)
        left, right = 1, 1
        for i in range(len(A)):
            res[i] *= left
            left *= A[i]
            res[len(A)-1-i] *= right
            right *= A[len(A)-1-i]
        return res
