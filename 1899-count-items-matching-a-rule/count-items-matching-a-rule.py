class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        j = 0
        if ruleKey == 'type':
            j = 0
        elif ruleKey == 'color':
            j = 1
        else:
            j = 2
        
        ans = 0

        for i in range(len(items)):
            if ruleValue == items[i][j]:
                ans += 1
        return ans        