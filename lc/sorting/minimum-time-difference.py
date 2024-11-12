class Solution:
    def convert_2_minutes(self, t):
        hh,mm = t.split(":")
        return int(hh) * 60 + int(mm)

    def findMinDifference(self, timePoints: List[str]) -> int:
        # complexity: time O(nlogn), space O(1)
        for i in range(len(timePoints)):
            timePoints[i] = self.convert_2_minutes(timePoints[i])
        timePoints = sorted(timePoints)
        res = sys.maxsize
        for i in range(len(timePoints)-1):
            res = min(res, timePoints[i+1] - timePoints[i])
        return min(res, 1440 - timePoints[-1] + timePoints[0])
