class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        v = []
        n = len(nums)
       
        for i in range(n):
            if nums[i] not in v and nums.count(nums[i]) > n/2:
                return nums[i]
            else:
                v.append(nums[i])    
                