class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        if num == 0:
            return True
        
        rev1 = 0
        temp = num
        while temp > 0:
            rev1 = rev1 * 10 + temp % 10
            temp //= 10

        rev2 = 0
        while rev1 > 0:
            rev2 = rev2 * 10 + rev1 % 10
            rev1 //= 10

        return num == rev2