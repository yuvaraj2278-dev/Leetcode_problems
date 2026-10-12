class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        s = []
        for i in range(n):
            s.append(sum(tasks[i]))
        return min(s)    