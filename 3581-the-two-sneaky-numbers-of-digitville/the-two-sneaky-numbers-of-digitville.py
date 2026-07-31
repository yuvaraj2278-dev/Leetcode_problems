class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums.count(nums[i]) >= 2 and nums[i] not in ans:
                ans.append(nums[i])
        return ans         