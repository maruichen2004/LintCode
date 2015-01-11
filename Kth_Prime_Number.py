class Solution:
    def kthPrimeNumber(self, k):
        if k < 0: return 0
        res = 0
        queue3, queue5, queue7 = [1], [], []
        for i in range(k+1):
            v3 = queue3[0] if len(queue3) > 0 else sys.maxint
            v5 = queue5[0] if len(queue5) > 0 else sys.maxint
            v7 = queue7[0] if len(queue7) > 0 else sys.maxint
            res = min(v3, v5, v7)
            if res == v3:
                queue3 = queue3[1:]
                queue3.append(3 * res)
                queue5.append(5 * res)
            elif res == v5:
                queue5 = queue5[1:]
                queue5.append(5 * res)
            elif res == v7:
                queue7 = queue7[1:]
            queue7.append(7 * res)
        return res
