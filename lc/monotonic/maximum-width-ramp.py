class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ramp = 0
        n = len(nums)
        st = deque()
        for i in range(n):
            if not st or nums[st[-1]] > nums[i]:
                st.append(i)

        for i in range(n-1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                ramp = max(ramp, i - st[-1])
                st.pop()
        return ramp