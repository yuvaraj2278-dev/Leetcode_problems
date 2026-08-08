class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows , cols = len(mat) , len(mat[0])
        c_rows = []
        c_cols = []

        for i in range(rows):
            c_rows.append(mat[i].count(1))
        
        j = 0

        for i in range(cols):
            count = 0
            j = 0
            while j < rows:
                if mat[j][i] == 1:
                    count += 1
                j += 1
            c_cols.append(count)   

        ans = 0     

        for i in range(len(c_rows)):
            if c_rows[i] == 1:
                for j in range(len(c_cols)):
                    if mat[i][j] == 1:
                        if c_cols[j] == 1:
                            ans += 1
            

        return ans              



            



    