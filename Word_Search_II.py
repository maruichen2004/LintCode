class Solution:
    def wordSearchII(self, board, words):
        res = []
        for word in words:
            visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
            for i in range(len(board)):
                j = 0
                while j < len(board[0]):
                    if self.wordSearchHelper(board, word, visited, i, j):
                        res.append(word)
                        break
                    j += 1
                if j < len(board[0]): break
        return res
        
    def wordSearchHelper(self, board, word, visited, i, j):
        if len(word) == 0: return True
        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or visited[i][j] == 1 or board[i][j] != word[0]:
            return False
        visited[i][j] = 1
        found = self.wordSearchHelper(board, word[1:], visited, i - 1, j) or \
                self.wordSearchHelper(board, word[1:], visited, i + 1, j) or \
                self.wordSearchHelper(board, word[1:], visited, i, j - 1) or \
                self.wordSearchHelper(board, word[1:], visited, i, j + 1)
        visited[i][j] = 0
        return found
