class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # greedy + sorting + heap
        # time O(qlogq + n(logq+logn)), space O(n)
        avail = [] # max heap => greedy get largest idx
        cur = [] # min heap => remove min id
        n = len(nums)
        queries = sorted(queries, reverse=True) # pop() faster than pop(0)
        for i in range(n):
            while queries and queries[-1][0] <= i:
                heappush(avail, -queries[-1][1])
                queries.pop()
            while cur and cur[0] < i:
                heappop(cur)
            while len(cur) < nums[i]:
                if len(avail) == 0 or -avail[0] < i: return -1
                max_idx = -heappop(avail)
                heappush(cur, max_idx)
        
        return len(avail)