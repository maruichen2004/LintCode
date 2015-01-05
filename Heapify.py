class Solution:
    def heapify(self, A):
        for i in reversed(range(len(A)/2+1)):
            self.shiftDown(A, i)
            
    def shiftDown(self, A, i):
        left = i * 2 + 1
        right = i * 2 + 2
        while left < len(A) or right < len(A):
            leftVal = A[left] if left < len(A) else sys.maxint
            rightVal = A[right] if right < len(A) else sys.maxint
            next = left if leftVal <= rightVal else right
            if A[i] < A[next]: break
            else:
                A[i], A[next] = A[next], A[i]
                i = next
                left = 2 * i + 1
                right = 2 * i + 2
