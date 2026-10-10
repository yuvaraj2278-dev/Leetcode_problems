class Solution:
    def removeZeros(self, n: int) -> int:
        ans = 0
        while n > 0:
            d = n%10
            if d != 0:
                ans = ans*10 + d
            n //= 10
        
        rev =  0
        while ans > 0:
            d = ans%10
            rev = rev*10 + d
            ans //= 10
        return rev    
                    