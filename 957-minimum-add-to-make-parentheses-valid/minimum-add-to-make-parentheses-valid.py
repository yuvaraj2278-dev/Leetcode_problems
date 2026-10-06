class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        add = 0
        for i in range(len(s)):
            if s[i] == '(':
                ans += 1
            else:
                if ans > 0:
                    ans -= 1
                else:
                    add += 1     
        return ans + add           