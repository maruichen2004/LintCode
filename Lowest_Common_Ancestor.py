class Solution:
    def lowestCommonAncestor(self, root, A, B):
        if root is None: return None
        if root == A or root == B: return root
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        if left is not None and right is not None: return root
        return left if left is not None else right
