class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        miss = 0
        rep = 0
        ans = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans.append(grid[i][j])

        for i in range(len(ans)):
            if ans.count(ans[i]) >= 2:
                rep = ans[i]
                break        


        for i in range(1 , len(ans) + 1):
            if i not in ans:
                miss = i
                break

        return [rep,miss]            
