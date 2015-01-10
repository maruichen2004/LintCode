class Solution:
    def singleNumberIII(self, A):
        x = A[0]
        n1, n2 = 0, 0
        for i in range(1, len(A)):
            x ^= A[i]
        set_bit = x & (~(x - 1))
        for i in range(len(A)):
            if A[i] & set_bit: n1 ^= A[i]
            else: n2 ^= A[i]
        return (n1, n2)
