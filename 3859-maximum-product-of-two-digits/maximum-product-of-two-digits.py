class Solution:
    def maxProduct(self, n: int) -> int:
        nums = list(str(n))
        nums.sort()
        return int(nums[-1])*int(nums[-2])