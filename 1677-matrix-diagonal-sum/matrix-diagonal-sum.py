class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        j = -1
        ans = 0
        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][j]
            j -= 1
        return ans - (mat[ n // 2][n // 2] if n%2 != 0 else 0 )    


