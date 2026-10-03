class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = []
        n = len(nums)
        for i in range(n//2):
            mn = min(nums)
            mx = max(nums)
            avg.append((mn+mx)/2)
            nums.remove(mn)
            nums.remove(mx)
        return min(avg)    
