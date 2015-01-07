class Solution:
    def sortLetters(self, chars):
        if len(chars) <= 1: return
        i, j = 0, len(chars) - 1
        while i < len(chars) and "a" <= chars[i] <= "z": i += 1
        while j >= 0 and "A" <= chars[j] <= "Z": j -= 1
        while i < j:
            chars[i], chars[j] = chars[j], chars[i]
            while i < len(chars) and "a" <= chars[i] <= "z": i += 1
            while j >= 0 and "A" <= chars[j] <= "Z": j -= 1
