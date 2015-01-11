class Solution:
    def rerange(self, A):
        if A is None or len(A) <= 1: return A
        poscount = 0
        for i in range(len(A)): 
            if A[i] > 0: poscount += 1
        negP = 1 if poscount > len(A) - poscount else 0
        posP = 0 if poscount > len(A) - poscount else 1
        p = len(A) - 1
        while negP < len(A) and A[negP] < 0: negP += 2
        while posP < len(A) and A[posP] > 0: posP += 2
        while p >= negP or p >= posP:
            if A[p] < 0:
                if negP >= len(A): p -= 1
                else:
                    A[negP], A[p] = A[p], A[negP]
                    negP += 2
            else:
                if posP >= len(A): p -= 1
                else:
                    A[posP], A[p] = A[p], A[posP]
                    posP += 2
        return A
