class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            d_sum = 0
            d = nums[i]
            while d > 0:
                d_sum += d%10
                d //= 10
            if d_sum == i:
                return i
        return -1            

