class MinStack(object):
    def __init__(self):
        self.s = []
        
    def push(self, number):
        if len(self.s) == 0: self.s.append((number, number))
        else: self.s.append((number, min(number, self.s[-1][1])))
        
    def pop(self):
        if len(self.s) == 0: print "empty stack"
        else:
            val = self.s[-1][0]
            self.s.pop()
            return val
            
    def min(self):
        if len(self.s) == 0: print "empty stack"
        else: return self.s[-1][1]
