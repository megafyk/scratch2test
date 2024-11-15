class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # monotonic stack
        # time O(n), space O(n)
        n = len(nums)
        second = -sys.maxsize
        dq = deque()
        for i in range(n-1, -1,-1):
            if nums[i] < second:
                return True
            while dq and dq[-1] < nums[i]:
                second = dq.pop()
            dq.append(nums[i])
        return False
