class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(s) != len(words):
            return False
        j = 0
        for i in words:
            if s[j] != i[0]:
                return False
            j += 1    
        return True            