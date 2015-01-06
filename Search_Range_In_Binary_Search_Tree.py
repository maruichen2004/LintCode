class Solution:
    def searchRange(self, root, k1, k2):
        return self.searchRangeHelper(root, k1, k2)
        
    def searchRangeHelper(self, cur, k1, k2):
        res = []
        if cur is None: return res
        if k1 > k2: return res
        left = self.searchRangeHelper(cur.left, k1, min(cur.val-1, k2))
        right = self.searchRangeHelper(cur.right, max(cur.val+1, k1), k2)
        res += left
        if k1 <= cur.val <= k2: res.append(cur.val)
        res += right
        return res
