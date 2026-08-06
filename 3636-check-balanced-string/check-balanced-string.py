class Solution:
    def isBalanced(self, num: str) -> bool:
        n = int(num)
        digit_list = [int(d) for d in str(n)]
        os = 0
        es = 0
        for i in range(len(digit_list)):
            if i%2 == 0:
                es += digit_list[i]
            else:
                os += digit_list[i]
        return os == es             
