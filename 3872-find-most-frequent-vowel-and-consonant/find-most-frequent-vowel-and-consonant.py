class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = ['a','e','i','o','u']
        v_f = []
        c_f = []
        vist = []

        for i in s:
            if i in v and i not in vist:
                v_f.append(s.count(i)) 
                vist.append(i)
            elif i not in v and i not in vist :
                c_f.append(s.count(i))
                vist.append(i)  
        return max(v_f,default = 0) + max(c_f, default = 0)        