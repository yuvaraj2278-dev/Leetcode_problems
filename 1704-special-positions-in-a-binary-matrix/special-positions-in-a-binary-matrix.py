class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows , cols = len(mat) , len(mat[0])
        c_rows = [0]*rows
        c_cols = [0]*cols
        ans = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    c_rows[i] += 1
                    c_cols[j] += 1

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    if c_rows[i] == 1 and c_cols[j] == 1:
                        ans += 1

        return ans                
