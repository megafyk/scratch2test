class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # sorting + 2 pointers
        # time O(nlogn), space O(1)
        mod = 10**9 + 7
        nums = sorted(nums)
        cnt_sub = 0

        n = len(nums)
        i, j = 0, n - 1
        # pre process
        p = [1] * n
        for t in range(1, n):
            p[t] = (p[t - 1] * 2) % mod

        while i <= j:
            if nums[i] + nums[j] <= target:

                cnt_sub = (
                    cnt_sub + p[j - i]
                ) % mod  # from i->j,choose include i+1 in subseq or not -> 2^(j-i)
                i += 1
            else:
                j -= 1

        return cnt_sub % mod
