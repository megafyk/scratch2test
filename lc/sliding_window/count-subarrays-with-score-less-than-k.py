class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        # sliding window
        # time O(N), space O(1)
        N = len(nums)
        s = 0
        i = 0
        res = 0
        for j in range(N):
            s += nums[j]
            while i <= j and s * (j - i + 1) >= k:
                s -= nums[i]
                i += 1

            res += j - i + 1
        return res

    # def countSubarrays(self, nums: List[int], k: int) -> int:
    #     # prefix sum + binary search
    #     # time O(NlogN), space O(N)
    #     N = len(nums)
    #     prefix = [0] * N
    #     prefix[0] = nums[0]
    #     for i in range(1, N):
    #         prefix[i] = prefix[i-1] + nums[i]

    #     def search(l,r):
    #         idx = r
    #         while l <= r:
    #             m = (l+r) // 2
    #             tmp = 0 if m == 0 else prefix[m-1]
    #             if (prefix[idx] - tmp) * (idx - m + 1) >= k:
    #                 l = m + 1
    #             else:
    #                 r = m - 1
    #         return l

    #     res = 0
    #     for i in range(N):
    #         pos = search(0, i)
    #         if pos > i: continue
    #         res += (i-pos+1)
    #     return res
