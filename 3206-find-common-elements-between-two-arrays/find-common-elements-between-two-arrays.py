class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans1 = 0
        ans2 = 0

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans1 += 1

        for i in range(len(nums2)):
            if nums2[i] in nums1:
                ans2 += 1        
        return [ans1,ans2]        