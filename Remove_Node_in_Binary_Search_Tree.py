class Solution:
    def removeNode(self, root, value):
        if root is None: return root
        parent, cur = None, root
        while cur and cur.val != value:
            parent = cur
            if cur.val < value: cur = cur.right
            else: cur = cur.left
        if cur is None: return root
        if cur.left is None and cur.right is None:
            if parent is None: return None
            if parent.left == cur: parent.left = None
            elif parent.right == cur: parent.right = None
        elif cur.left is None or cur.right is None:
            if parent is None: 
                root = cur.right if cur.left is None else cur.left
            elif parent.left == cur:
                parent.left = cur.right if cur.left is None else cur.left
            else:
                parent.right = cur.right if cur.left is None else cur.left
        else:
            prevParent, prev = None, cur.left
            while prev.right:
                prevParent = prev
                prev = prev.right
            cur.val = prev.val
            if prev.left is None:
                if prevParent is None: cur.left = None
                else: prevParent.right = None
            else:
                if prevParent is None: cur.left = prev.left
                else: prevParent.right = prev.left
        return root
