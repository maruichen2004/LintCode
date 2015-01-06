class Solution:
    def __init__(self, root):
        self.stack = []
        self.cur = root

    def hasNext(self):
        return len(self.stack) != 0 or self.cur

    def next(self):
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        parent = self.stack.pop()
        self.cur = parent.right
        return parent
