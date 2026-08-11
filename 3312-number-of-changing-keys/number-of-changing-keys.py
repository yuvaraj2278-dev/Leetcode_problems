class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        count = 0
        left = 0
        right = 1

        while right < len(s):
            if s[left] != s[right]:
                count += 1
            left += 1
            right += 1
        return count         