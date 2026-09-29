class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        a1 = startTime.split(":")
        a2 = endTime.split(":")
        st = 0
        et = 0

        st += int(a1[0]) * 3600
        st += int(a1[1]) * 60
        st += int(a1[2])

        et += int(a2[0]) * 3600
        et += int(a2[1]) * 60
        et += int(a2[2])

        return et - st        
        