class Solution:
    def serialize(self, root):
        res = []
        self.serializeHelper(root, res)
        return res

    def serializeHelper(self, root, res):
        if root is None:
            res.append(None)
            return
        res.append(root.val)
        self.serializeHelper(root.left, res)
        self.serializeHelper(root.right, res)

    def deserialize(self, data):
        stack = []
        for num in reversed(data):
            if num is None: stack.append(None)
            else:
                left = stack.pop()
                right = stack.pop()
                root = TreeNode(num)
                root.left = left
                root.right = right
                stack.append(root)
        return stack[-1]
