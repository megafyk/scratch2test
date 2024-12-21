class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # increasing monotonic stack
        # time O(n), space O(n)
        n = len(heights)
        st = deque()
        res = 0

        for idx, height in enumerate(heights):
            start = idx
            while st and st[-1][1] > height:
                i,h = st.pop()
                res = max(res, (idx-i) * h)
                start = i
            st.append((start, height))

        for idx, height in st:
            res = max(res, height * (len(heights) - idx))
        return res
