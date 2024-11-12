class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # sorting
        # time O(nlogn), space O(n)
        new_queries = sorted([(val, i) for i,val in enumerate(queries)])
        items = sorted(items)
        n = len(items)
        i = 0
        curr_max = 0
        ans = [0] * len(queries)
        for q,idx in new_queries:
            while i < n and items[i][0] <= q:
                curr_max = max(curr_max, items[i][1])
                i += 1
            ans[idx] = curr_max
        return ans
