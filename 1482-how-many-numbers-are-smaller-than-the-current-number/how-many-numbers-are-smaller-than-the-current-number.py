class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        count = 0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            ans.append(count)
            count = 0
        return ans            