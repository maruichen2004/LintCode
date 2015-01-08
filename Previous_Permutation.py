class Solution:
    def previousPermuation(self, num):
        k, l = len(num), 0
        for i in range(len(num) - 1):
            if num[i] > num[i+1]: k = i
        if k == len(num): return num[::-1]
        for i in range(len(num)):
            if num[i] < num[k]: l = i
        num[k], num[l] = num[l], num[k]
        return num[:k+1] + num[:k:-1]
