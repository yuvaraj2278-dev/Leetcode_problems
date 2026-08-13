class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            s = str(i)
            for i in range(len(s)):
                ans.append(int(s[i]))
        return ans        