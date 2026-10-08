class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = 0
        result = ""
        for i in range(len(s)-1):
            if s[i] == '(':
                if ans > 0:
                    result += s[i] 
                ans += 1
            else:
                if ans != 1:
                    result += s[i]
                ans -= 1     
        return result         

