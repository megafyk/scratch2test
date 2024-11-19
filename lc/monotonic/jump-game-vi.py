class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        # complexity: time O(n), time O(n)
        n = len(nums)
        st = deque()
        st.append(0)

        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            if st[0] < i - k:
                st.popleft()
            dp[i] = dp[st[0]] + nums[i]
            while st and dp[st[-1]] <= dp[i]:
                st.pop()
            st.append(i)

        return dp[-1]