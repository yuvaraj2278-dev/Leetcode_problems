class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []
        for i in range(left,right+1):
            temp = i
            flag = 0
            while temp > 0:
                d = temp%10
                if d == 0:
                    break
                if i%d == 0:
                    flag += 1
                else:
                    break

                temp //= 10             
            if flag == len(str(i)):
                ans.append(i)
        return ans        
