class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        f = 0
        if len(word1) > len(word2):
            n = len(word2)
            f = 1
        else:
            n = len(word1) 
            f = 2

        for i in range(n):
                ans.append(word1[i])
                ans.append(word2[i])
 
        if f == 1:
            ans.extend(word1[n:])
        else:
            ans.extend(word2[n:])            


        return "".join(ans)    


