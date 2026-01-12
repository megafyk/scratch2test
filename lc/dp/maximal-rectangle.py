class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # dp + increasing monotonic stack
        # time O(m*n), space O(m*n)
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j] + 1 if matrix[i-1][j] == "1" else 1

        # find max rectangle in histogram
        res = 0
        for row in dp:
            st = deque()
            for idx, height in enumerate(row):
                start = idx
                while st and st[-1][1] > height:
                    i,h = st.pop()
                    res = max(res, (idx-i) * h)
                    start = i
                st.append((start, height))

            for idx, height in st:
                res = max(res, (len(row) - idx) * height)
        return res


class Solution1:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # dp
        # time O(m*n*n), space O(n^2)
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n+1) for _ in range(n)]
        res = 0
        
        for i in range(m):
            nw_dp = [[0] * (n+1) for _ in range(n)]
            r_l = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    r_l +=1
                    for l in range(1, r_l + 1):
                        nw_dp[j][l] = dp[j][l] + l
                        res = max(res, nw_dp[j][l])
                else:
                    r_l = 0
            dp = nw_dp
        return res