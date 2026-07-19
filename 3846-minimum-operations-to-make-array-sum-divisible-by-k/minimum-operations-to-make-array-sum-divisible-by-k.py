class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        count = 0
        while s%k != 0:
            count += 1
            s -= 1
        return count    