from math import gcd
class Solution:
    
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mx = 0
        for i in range(len(nums)):
            mx = max(mx, nums[i])
            prefixGcd.append(gcd(nums[i], mx))
        prefixGcd.sort()
        
        left = 0
        right = len(prefixGcd) - 1
        sum = 0

        while left < right:
            sum += gcd(prefixGcd[left],prefixGcd[right])
            left += 1
            right -= 1
        return sum    