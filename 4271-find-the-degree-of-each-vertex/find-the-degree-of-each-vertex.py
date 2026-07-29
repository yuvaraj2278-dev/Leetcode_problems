class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        for i in range(len(matrix)):
            ans.append(sum(matrix[i]))
        return ans    