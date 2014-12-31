class Solution:
    def findPeak(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            mid = (i + j) / 2
            if (mid == 0 or A[mid] > A[mid-1]) and (mid == len(A) - 1 or A[mid] > A[mid+1]):
                return mid
            elif mid > 0 and A[mid-1] > A[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return i
