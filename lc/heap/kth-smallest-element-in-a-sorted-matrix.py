class Solution:
    import heapq
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # complexity O(klogn), mem O(k)
        minheap = []
        n = len(matrix)
        for i in range(n):
            heapq.heappush(minheap, (matrix[i][0], i, 0))
        for _ in range(k):
            res, i, j = heapq.heappop(minheap)
            if j < n-1:
                heapq.heappush(minheap, (matrix[i][j+1], i, j+1))
        return res
    # def check(self, matrix, n, mid, k):
    #     cnt = 0
    #     j = n-1
    #     for i in range(n):
    #         while j >= 0 and matrix[i][j] > mid:
    #             j -= 1
    #         cnt += j + 1
    #     return cnt < k

    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     # complexity O(n^2logn), mem O(1)
    #     n = len(matrix)
    #     l, r = matrix[0][0], matrix[n-1][n-1]
    #     while l < r:
    #         m = l + (r - l) // 2
    #         if self.check(matrix, n, m, k):
    #             l = m + 1
    #         else:
    #             r = m
    #     return l
    # import heapq
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     # complexity O(n^2logk), mem O(k)
    #     maxheap = []
    #     n = len(matrix)
    #     for row in range(n):
    #         for col in range(n):
    #             val = -matrix[row][col]
    #             if len(maxheap) < k:
    #                 heapq.heappush(maxheap, val)
    #             elif val > maxheap[0]:
    #                 heapq.heappush(maxheap, val)
    #                 heapq.heappop(maxheap)
    #     return -maxheap[0]