class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        costs.sort()
        for i in costs:
            if coins-i >= 0:
                coins -= i
                ans += 1
            if i > coins:
                return ans     
        return ans          

