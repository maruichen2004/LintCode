class Solution:
    def kthLargestElement(self, k, A):
        return self.quickSelect(A, k-1)
        
    def quickSelect(self, A, k):
        i, j = 0, len(A) - 1
        while i <= j:
            mid = (i + j) / 2
            idx = self.partition(A, i, j, mid)
            if idx == k: return A[idx]
            elif idx < k: i = idx + 1
            else: j = idx - 1
        return -1
        
    def partition(self, A, start, end, p):
        pivot = A[p]
        A[end], A[p] = A[p], A[end]
        idx = start
        for i in range(start, end):
            if A[i] > pivot:
                A[i], A[idx] = A[idx], A[i]
                idx += 1
        A[idx], A[end] = A[end], A[idx]
        return idx
