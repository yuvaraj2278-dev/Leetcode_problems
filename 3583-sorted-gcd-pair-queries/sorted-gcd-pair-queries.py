from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = numbers divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        # exact[d] = number of pairs with gcd exactly d
        exact = [0] * (mx + 1)

        # Process from largest gcd to smallest
        for d in range(mx, 0, -1):
            pairs = cnt[d] * (cnt[d] - 1) // 2
            multiple = 2 * d
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += d
            exact[d] = pairs

        # Prefix counts
        prefix = []
        gcd_values = []

        total = 0
        for d in range(1, mx + 1):
            if exact[d] > 0:
                total += exact[d]
                prefix.append(total)
                gcd_values.append(d)

        # Answer queries
        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(gcd_values[idx])

        return ans