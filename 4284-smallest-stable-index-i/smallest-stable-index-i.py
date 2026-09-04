class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        si = 0
        for i in range(n):
            l = max(nums[0:i+1])
            s = min(nums[i:n])
            si = l-s
            if si <= k:
                return i
        return -1        
