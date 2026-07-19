class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ls = sum(nums[:i])
            rs = sum(nums[i+1:])
            a = abs(ls - rs)
            ans.append(a)
        return ans    
