class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_f = 0
        for i in range(len(nums)):
            c = nums.count(nums[i])
            if c > max_f:
                max_f = c
        ans = 0
        v = []
        for i in range(len(nums)):
            c = nums.count(nums[i])
            if c == max_f and nums[i] not in v:
                ans += max_f
                v.append(nums[i])

        return ans         