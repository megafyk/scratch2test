class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # double dp
        # complexity: time O(n*m), mem O(m)
        n, m = len(points), len(points[0])
        ans = points[0][0]
        prev_row = points[0]

        for i in range(1, n):
            dp_left, dp_right = [0] * m, [0] * m

            dp_left[0] = prev_row[0]
            dp_right[-1] = prev_row[-1]

            for j in range(1, m):
                dp_left[j] = max(dp_left[j - 1] - 1, prev_row[j])

            for j in range(m - 2, -1, -1):
                dp_right[j] = max(dp_right[j + 1] - 1, prev_row[j])

            nx_row = list(points[i])

            for j in range(m):
                nx_row[j] += max(dp_left[j], dp_right[j])
            prev_row = nx_row

        return max(prev_row)
