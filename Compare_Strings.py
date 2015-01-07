class Solution:
    def compareStrings(self, A, B):
        map = {}
        for ch in B:
            if ch not in map: map[ch] = 1
            else: map[ch] += 1
        for ch in A:
            if ch in map:
                if map[ch] > 0: map[ch] -= 1
        for item in map:
            if map[item] > 0: return False
        return True
