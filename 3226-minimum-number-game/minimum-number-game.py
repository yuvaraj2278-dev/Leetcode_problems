class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        l = len(nums)
        for i in range(l//2):
            a = min(nums)
            nums.remove(a)
            b = min(nums)
            nums.remove(b)
            arr.append(b)
            arr.append(a)
        return arr    