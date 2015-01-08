class Solution:
    def checkPowerOf2(self, n):
        if n <= 0: return False
        return True if n & (n-1) == 0 else False
