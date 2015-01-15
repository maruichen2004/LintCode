class Solution:
    def topSort(self, graph):
        unvisited = set(graph)
        res = []
        while unvisited:
            cur = unvisited.copy().pop()
            self.dfs(cur, unvisited, res)
        return res
        
    def dfs(self, cur, unvisited, res):
        for nbr in cur.neighbors:
            if nbr in unvisited:
                self.dfs(nbr, unvisited, res)
        res.insert(0, cur)
        unvisited.remove(cur)
