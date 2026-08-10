class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i].isdigit():
                s[i] = chr( ord(s[i-1]) + int(s[i]) )
        return "".join(s)        
