class Solution:
    def hashCode(self, key, HASH_SIZE):
        if len(key) == 0: return 0
        res, base = 0, 1
        for i in reversed(range(len(key))):
            res += ord(key[i]) * base % HASH_SIZE
            res %= HASH_SIZE
            base = base * 33 % HASH_SIZE
        return res
