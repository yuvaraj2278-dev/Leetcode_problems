class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = sum(nums)
        d_s = 0
        for i in nums:
            n = i
            while n > 0:
                d_s += n%10
                n //= 10
        return abs(s - d_s)        
