class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, element):
        self.stack1.append(element)
        
    def top(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) != 0:
            return self.stack2[-1]
        
    def pop(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) != 0:
            return self.stack2.pop()
