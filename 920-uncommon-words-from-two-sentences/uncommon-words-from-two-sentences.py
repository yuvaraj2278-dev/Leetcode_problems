class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = s1.split()
        l2 = s2.split()
        ans = l1 + l2
        a = []

        for i in ans:
            if ans.count(i) == 1:
                a.append(i)      

        return a       
