class Solution:
    def maxDepth(self, s: str) -> int:
        ans = []
        n = len(s)
        flag = 0
        for i in range(n):
            if s[i] == "(":
                flag += 1
            if s[i] == ")":
                ans.append(flag)
                flag -= 1
        if len(ans) == 0:
            return 0        
        return max(ans)        
            