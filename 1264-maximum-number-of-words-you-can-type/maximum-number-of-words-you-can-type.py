class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l = text.split()
        ans = 0
        w = list(brokenLetters)

        for i in l:
            for j in range(len(i)):
                if i[j] in w:
                    break
            else:        
                ans += 1
        return ans             