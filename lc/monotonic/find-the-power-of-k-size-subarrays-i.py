class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # monotonic stack
        # time O(n), space O(n)
        power = []

        st = deque()
        n = len(nums)
        for i in range(k-1):
            while st and (st[-1][0] + 1 != nums[i] or st[-1][1] + 1 != i):
                st.pop()
            st.append((nums[i], i))

        for i in range(k-1, n):
            while st and (st[-1][0] + 1 != nums[i] or st[-1][1] + 1 != i):
                st.pop()
            st.append((nums[i], i))
            if len(st) >=  k:
                if len(st) > k:
                    st.popleft()
                power.append(st[-1][0])
            else:
                power.append(-1)

        return power
