class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        v = []
        flag = 0
        for i in range(len(arr)):
            if arr.count(arr[i]) == 1 and arr[i] not in v:
                v.append(arr[i])
                flag += 1
                if flag == k:
                    return  arr[i]
        return ""            