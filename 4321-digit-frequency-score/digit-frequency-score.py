class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        v = []
        score = 0
        while n > 0:
            d = n%10
            if d not in v:
                score += d*(str(n).count(str(d)))
                v.append(d)
            n //= 10    
        return score        

