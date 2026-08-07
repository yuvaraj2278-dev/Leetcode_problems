class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        for i in range(len(ransomNote)):
            if ransomNote.count(ransomNote[i]) <= magazine.count(ransomNote[i]):
                continue
            else:
                return False
        return True            