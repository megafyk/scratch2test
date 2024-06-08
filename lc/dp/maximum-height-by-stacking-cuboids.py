class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # DP + sort
        # complexity: time O(n^2), mem O(n)
        n = len(cuboids)
        for cuboid in cuboids:
            cuboid.sort()
        cuboids.sort()
        dp = []
        for i in range(n):
            dp.append(cuboids[i][2])

        for i in range(1, n):
            for j in range(0, i):
                if (
                    cuboids[i][0] >= cuboids[j][0]
                    and cuboids[i][1] >= cuboids[j][1]
                    and cuboids[i][2] >= cuboids[j][2]
                ):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])

        return max(dp)
