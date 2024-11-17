class Solution:

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # prefix sum + monotonic deque
        # time O(n), space O(n)
        n = len(nums)
        cur_sum = 0
        res = n + 1
        q = deque()
        for i in range(n):
            cur_sum += nums[i]
            if cur_sum >= k:
                res = min(res, i + 1)
            while q and cur_sum - q[0][0] >= k:
                _, idx = q.popleft()
                res = min(res, i - idx)
            # maintain increasing monotonic
            while q and q[-1][0] >= cur_sum:
                q.pop()

            q.append((cur_sum, i))

        return -1 if res == n + 1 else res
