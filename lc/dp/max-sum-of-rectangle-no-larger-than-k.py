class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # dp with prefix sum
        # time O(n^2*mlogm), space O(m*n)
        m = len(matrix)
        n = len(matrix[0])

        presums = []
        for i in range(m):
            presum = [0] * n
            for j in range(n):
                presum[j] = presum[j-1] + matrix[i][j] if j > 0 else matrix[i][j]
            presums.append(presum)

        def find_max(arr):
            sorted_sum = [0]
            cur_sum = 0
            res = -sys.maxsize
            for num in arr:
                cur_sum += num
                target_sum = cur_sum - k
                idx = bisect.bisect_left(sorted_sum, target_sum)

                if idx < len(sorted_sum):
                    res = max(res, cur_sum - sorted_sum[idx])

                if res == k:
                    return res

                bisect.insort(sorted_sum, cur_sum)
            return res

        res = -sys.maxsize

        for c1 in range(n):
            for c2 in range(c1+1):
                # merge rows between c1 and c2
                cursum = [0] * m
                for i in range(m):
                    cursum[i] = presums[i][c1] - (presums[i][c2-1] if c2 > 0 else 0)
                res = max(res, find_max(cursum))
                if res == k:
                    return k
        return res
