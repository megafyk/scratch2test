class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        # greedy array interval
        # time O(m+n), space O(1)
        m, n = len(landStartTime), len(waterStartTime)
        mi_end_land, mi_end_water = inf, inf
        for i in range(m):
            mi_end_land = min(mi_end_land, landStartTime[i] + landDuration[i])
        for i in range(n):
            mi_end_water = min(mi_end_water, waterStartTime[i] + waterDuration[i])
        mi_land, mi_water = inf, inf

        for i in range(m):
            mi_water = min(
                mi_water, max(mi_end_water, landStartTime[i]) + landDuration[i]
            )
        for i in range(n):
            mi_land = min(
                mi_land, max(mi_end_land, waterStartTime[i]) + waterDuration[i]
            )

        return min(mi_land, mi_water)
