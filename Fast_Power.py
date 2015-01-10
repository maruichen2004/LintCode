class Solution:
    def fastPower(self, a, b, n):
        res = self.power(a, b, n)
        return int(res)
        
    def power(self, a, b, n):
        if a == 0: return 0
        if n == 0: return 1 % b
        res = self.power(a, b, n/2)
        res *= res
        res %= b
        if n % 2 == 1: res *= (a % b)
        res %= b
        return res
