class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # binary search + math
        # n = len(workerTimes)
        # m = mountainHeight * max(workerTimes)
        # time O(nlogm), space O(1)
        l,r = 1, (mountainHeight * (mountainHeight + 1)) // 2 * max(workerTimes)

        def check(time):
            h = 0
            for w in workerTimes:
                delta_sq = math.floor((1 + 8*time/w) ** 0.5)
                h += (-1+delta_sq) // 2
            return h >= mountainHeight

        while l < r:
            mid = l + (r-l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l