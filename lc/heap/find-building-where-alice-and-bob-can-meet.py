class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # min heap brute force -> optimize loop use min heap
        # space O(q + nlogq), space O(q)
        res = [-1] * len(queries)
        groups = defaultdict(list)

        for idx, q in enumerate(queries):
            a,b = sorted(q)
            if a == b or heights[a] < heights[b]:
                res[idx] = b
            else:
                h = max(heights[a], heights[b])
                groups[b].append((h, idx))
        pq = []
        for idx, height in enumerate(heights):
            for q_h,q_i in groups[idx]:
                heappush(pq, (q_h, q_i))

            while pq and pq[0][0] < height:
                q_h, q_i = heappop(pq)
                res[q_i] = idx
        return res
