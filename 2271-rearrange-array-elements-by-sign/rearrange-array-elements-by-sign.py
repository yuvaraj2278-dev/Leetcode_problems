class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pa = []
        na = []
        ans = []
        for i in nums:
            if i < 0:
                na.append(i)
            else:
                pa.append(i)

        for i in range(len(pa)):
            ans.append(pa[i])
            ans.append(na[i])

        return ans                 