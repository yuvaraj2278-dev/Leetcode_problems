class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = []
        v = []
        for i in arr:
            if i not in v:
                if arr.count(i) not in a:
                    a.append(arr.count(i))
                    v.append(i)
                else:    
                    return False
        return True        
                