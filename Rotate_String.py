class Solution:
    def rotateString(self, A, offset):
        if len(A) == 0: return A
        strA = [i for i in A]
        offset %= len(A)
        self.reverseString(strA, 0, len(strA) - 1 - offset)
        self.reverseString(strA, len(strA) - offset, len(strA) - 1)
        self.reverseString(strA, 0, len(strA) - 1)
        return "".join(strA)
        
    def reverseString(self, A, start, end):
        while start < end:
            A[start], A[end] = A[end], A[start]
            start, end = start + 1, end - 1
