class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0: return 0
        i, j, res = 0, len(matrix[0]) - 1, 0
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                res += 1
                i += 1
                j -= 1
            elif matrix[i][j] > target: j -= 1
            else: i += 1
        return res
