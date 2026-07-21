class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left = 0 
        right = len(s)

        ans = []

        for i in s:
            if i == 'I':
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1
        if s[-1] == 'I':
            ans.append(ans[-1]+1)
        else:
            ans.append(ans[-1]-1)           
        return ans        
