class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        # monotonic stack
        # time O(n), space O(n)
        mod = 10 ** 9 + 7
        nums = [-sys.maxsize] + nums + [-sys.maxsize]
        n = len(nums)
        res = 0
        st = deque()
        for i in range(n):
            while st and st[-1][0] > nums[i]:
                num,j = st.pop()
                left = j - st[-1][1] if st else j+1
                right = i-j
                # num of sub contain num = combination left * right
                res = (res + num * (left * right)) % mod
            st.append((nums[i], i))
        return res

    # def sumSubarrayMins(self, nums: List[int]) -> int:
    #     # monotonic stack
    #     # time O(n), space O(n)
    #     mod = 10 ** 9 + 7
    #     n = len(nums)
    #     res = 0
    #     st = deque()
    #     for i in range(n):
    #         while st and st[-1][0] > nums[i]:
    #             num,j = st.pop()
    #             left = j - st[-1][1] if st else j+1
    #             right = i-j
    #             # num of sub contain num = combination left * right
    #             res = (res + num * (left * right)) % mod
    #         st.append((nums[i], i))

    #     for i in range(len(st)):
    #         num,j = st[i]
    #         left = j - st[i-1][1] if i > 0 else j+1
    #         right = n - j
    #         res = (res + num * (left * right)) % mod

    #     return res
