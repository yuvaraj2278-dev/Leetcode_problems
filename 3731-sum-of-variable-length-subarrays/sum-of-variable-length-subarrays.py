class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        i = 0
        st  = 0
        total = 0
        while i <= len(nums)-1:
            st = max(0,i-nums[i])
            total += sum(nums[st:i+1])
            i += 1
        return total    