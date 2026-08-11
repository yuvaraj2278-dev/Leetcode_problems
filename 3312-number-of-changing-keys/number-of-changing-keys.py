class Solution:
    def countKeyChanges(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1):
            if s[i] != s[i+1].lower() and s[i] != s[i+1].upper():
                ans += 1
        return ans        