class Solution:
    def insertNode(self, root, node):
        if root is None: return node
        prev, cur, dir = None, root, 0
        while cur:
            prev = cur
            if cur.val < node.val:
                cur = cur.right
                dir = 1
            else:
                cur = cur.left
                dir = 0
        if dir == 0: prev.left = node
        else: prev.right = node
        return root
