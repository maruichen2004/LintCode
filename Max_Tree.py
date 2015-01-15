class Solution:
    def maxTree(self, A):
        stk = []
        for num in A:
            cur = TreeNode(num)
            while stk and stk[-1].val <= cur.val:
                left_neighbor = stk.pop()
                left_neighbor.right = cur.left
                cur.left = left_neighbor
            stk.append(cur)
        pre = None
        while stk:
            cur = stk.pop()
            cur.right = pre
            pre = cur
        return pre
