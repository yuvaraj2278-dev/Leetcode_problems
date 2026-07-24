class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        f = 0
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    f += 1
                    continue
            if f == 0:
                ans += 1
            f = 0

        return ans                

