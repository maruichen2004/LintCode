class Solution:
    def maxTree(self, A):
        if len(A) == 0: return None
        stack = [TreeNode(A[0])]
        for i in range(1, len(A)):
            if A[i] <= stack[-1].val:
                node = TreeNode(A[i])
                stack.append(node)
            else:
                n1 = stack.pop()
                while stack and stack[-1].val < A[i]:
                    n2 = stack.pop()
                    n2.right = n1
                    n1 = n2
                node = TreeNode(A[i])
                node.left = n1
                stack.append(node)
        root = stack.pop()
        while stack:
            stack[-1].right = root
            root = stack.pop()
        return root
